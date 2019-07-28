from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms import SubmitField,StringField,IntegerField,PasswordField
from yoga.models import Inscriptos,Admin
from flask import redirect,url_for



class InscripcionesForm(FlaskForm):

    nombre = StringField('Nombre: ', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    email = StringField('E-mail: ', validators=[DataRequired(),Email()])
    telefono = IntegerField('Telefono de contacto: ', validators=[DataRequired()])
    submit =  SubmitField('Inscribirse')

    def check_email(self, field):
        if Inscriptos.query.filter_by(email=field.data).first():
            return redirect(url_for('users.inscripciones'))

    def check_curso(self,field):
        if not Inscriptos.query.filter_by(email=field.data).first().curso_pagado:
            print('desea pagar el curso?')
            return redirect(url_for('users.desea_cursar'))

class LoginForm(FlaskForm):

    email = StringField('E-mail: ', validators=[DataRequired()])
    password = PasswordField('Password: ',validators=[DataRequired()])
    submit = SubmitField('Log in')

    def check_email(self, field):
        if Admin.query.filter_by(email=field.data).first():
            raise ValidationError('El mail ya ha sido registrado')

class RegistroForm(FlaskForm):

    email = StringField('E-mail: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    def check_email(self, field):
        if Admin.query.filter_by(email=field.data).first():
            raise ValidationError('El mail ya ha sido registrado')

