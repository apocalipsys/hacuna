import functools
from typing import Callable
from flask import session,flash,redirect,url_for,current_app

def requires_admin(f: Callable)-> Callable:
    @functools.wraps(f)
    def decorated_function(*args,**kwargs):
        if session.get('email') != current_app.config.get('ADMIN',''):
            flash('Tenes que ser administrador para acceder a esta pagina')
            return redirect(url_for('users.login'))
        return f(*args,**kwargs)
    return decorated_function
