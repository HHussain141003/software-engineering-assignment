from functools import wraps
from flask import session, redirect, url_for, flash

# This file contains functions which might be used across different pages (e.g check if the user is logged in)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("You must be logged in to access this page.", "error")
            return redirect(url_for('login.login'))
        return f(*args, **kwargs)
    return decorated_function

