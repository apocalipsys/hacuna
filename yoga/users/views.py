from flask import Blueprint,render_template,flash,redirect,url_for,request,session
import stripe
from yoga.users.forms import InscripcionesForm,LoginForm, RegistroForm
from yoga.models import Inscriptos
from yoga import db
from yoga.models import Admin
from flask_login import login_user,logout_user,login_required
#from yoga.libs.sendemail import EnviarEmail


public_key = "pk_test_TYooMQauvdEDq54NiTphI7jx"

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


users = Blueprint('users',__name__)


@users.route('/users', methods=['GET','POST'])
def inscripciones():

    form = InscripcionesForm()

    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        session['email'] = form.email.data
        telefono = form.telefono.data
        user = Inscriptos(nombre,apellido,session['email'],telefono)
        if form.check_email(form.email):
            if form.check_curso(form.email):
                flash('Alumno ya suscripto a la base de datos, desea pagar el curso?', 'info')

                return render_template('desea.html',public_key=public_key)
            else:
                flash('El email ya existe y ha pagado el curso, ingrese uno diferente','danger')

                return render_template('inscripciones.html', form=form)

        db.session.add(user)
        db.session.commit()
        men = flash('Alumno inscripto','info')

        return render_template('procesando.html',public_key=public_key,men = men)



    return render_template('inscripciones.html', form = form)






@users.route('/login', methods=['GET','POST'])
def login():


    form = LoginForm()

    if form.validate_on_submit():
        print('sin error hasta aca1')


        user = Admin.query.filter_by(email=form.email.data).first()
        print('sin error hasta aca2')

        if user == None:
            print('sin error hasta aca3')

            return render_template('login.html', men=flash('Usuario o contrasenia invalidos','danger'),form=form)
        if user.check_password(form.password.data) and user.email == form.email.data:
            print('sin error hasta aca4')

            try:
                print('sin error hasta aca5')

                session['email'] = form.email.data
                print('sin error hasta aca6')

                login_user(user)
                print('sin error hasta aca7')

                flash('ENTRASTE','info')
            except:
                print('sin error hasta aca8')

                session.rollback()
                print('hubo una excepcion, y se hizo session.rollback()')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.home')

            return redirect(next)

    return render_template('login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('chau pichu','info')
    return redirect(url_for('core.home'))

@users.route('/register', methods = ['GET','POST'])
#@login_required
def register():

    form = RegistroForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print('sin error hasta aca1')
        if form.check_email(form.email):
            flash('El email ya existe')
            return render_template('registrar.html',form = form)
        print('sin error hasta aca2')

        user = Admin(email, password)
        print('sin error hasta aca3')

        db.session.add(user)
        print('sin error hasta aca4')

        db.session.commit()
        print('sin error hasta aca5')

        flash('Usuario agregado','info')
        return redirect(url_for('core.home'))


    return render_template('registrar.html',form = form)

@users.route('/desea')
def desea_cursar():
    return render_template('desea.html')


@users.route('/gracias', methods=['GET','POST'])
def gracias():

    return render_template('gracias.html')


@users.route('/pagos/<int:pagado>', methods=['POST'])
def pagos_curso(pagado):
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])
 #   print(f'parece que anda {pagado}')
 #   print(customer.email)
 #   for cus in customer:
 #       print(cus)
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=100,
        currency='usd',
        description='Master Yogui diplomatura'
    )

    confirmado = Inscriptos.query.filter_by(email=session['email']).first()
    #print(current_user)
    print(confirmado.email)
    for k,v in customer.items():
        print(k,v)

    confirmado.curso_pagado = pagado
    db.session.add(confirmado)
    db.session.commit()

    #aviso_inscripcion = EnviarEmail(session['email'])
    #aviso_inscripcion.send()

    return render_template('gracias.html',pagado=pagado,)
    #return redirect(url_for('users.gracias'))

@users.route('/listado')
@login_required
def listado():
    listado = Inscriptos.query.all()
    return render_template('listado.html',listado=listado)