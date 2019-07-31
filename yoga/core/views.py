from flask import Blueprint, render_template
#from yoga import login_manager
#from yoga.models import Admin,db

core = Blueprint('core',__name__)

#@login_manager.user_loader
#def load_user(user_id):
#    return Admin.query.get(user_id)
    #return db.session.query(Admin).get(user_id)

@core.route('/', methods=['GET','POST'])
def home():
    print('aver aver aver si llega aca')
    return render_template('index.html')

@core.route('/contacto')
def contacto():
    return render_template('contact.html')\

@core.route('/visitanos')
def visitanos():
    return render_template('visitanos.html')

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/loquehacemos')
def loquehacemos():
    return render_template('servicios.html')