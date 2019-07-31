from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SECRET_KEY'] = os.urandom(64)
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://martincholoco:1qaz2wsx@localhost/hacuna'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

##LOGIN CONFIGURATION
from yoga.models import Admin

login_manager = LoginManager()
login_manager.login_message = 'Debe ser administrador para ingresar a esta pagina'
login_manager.login_message_category = 'danger'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)

login_manager.login_view = 'users.login'



############################################33
#import click
#from flask.cli import with_appcontext
#from yoga import db

try:
    db.create_all()
except:
    pass

###############################################

###core blueprint####
from yoga.core.views import core
app.register_blueprint(core)
### users bluerprint####
from yoga.users.views import users
app.register_blueprint(users)
