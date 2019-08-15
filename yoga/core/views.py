from flask import Blueprint, render_template
#from yoga import login_manager
#from yoga.models import Admin,db

core = Blueprint('core',__name__)


@core.route('/')
def home():
    return render_template('index.html')

@core.route('/contacto')
def contacto():
    return render_template('contact.html')

@core.route('/visitanos')
def visitanos():
    return render_template('visitanos.html')

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/loquehacemos')
def loquehacemos():
    return render_template('servicios.html')
