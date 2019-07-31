from yoga import db
from sqlalchemy import Column,Integer,String,Boolean
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from yoga import login_manager

class Inscriptos(db.Model):

    __tablename__ = 'inscriptos'

    id = Column(Integer,primary_key=True,unique=True)
    nombre = Column(String(20))
    apellido = Column(String(20))
    email = Column(String(40))
    telefono = Column(Integer)
    curso_pagado = Column(Boolean,default=0)

    def __init__(self,nombre,apellido,email,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        pagado = 'SI' if self.curso_pagado else 'NO'
        return f'E-mail del inscripto es: {self.email}\n Curso pagado: {pagado}'


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)



class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'
    id = Column(Integer,primary_key=True,unique=True)
    email = Column(String(40))
    password_hash = Column(String(128))

    def __init__(self,email,password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)