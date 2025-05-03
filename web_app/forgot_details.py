from flask import Blueprint, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from .database import get_db
import logging
import sqlite3
import smtplib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

forgot_details_bp = Blueprint("forgot_details", __name__, url_prefix='/forgot')

def get_user_by_username_or_email(user_input):
    db = get_db()
    db.row_factory = sqlite3.Row  # This lets you access columns by name
    cursor = db.cursor()

    query = '''
    SELECT * FROM users
    WHERE username = ? OR email = ?
    '''
    cursor.execute(query, (user_input, user_input))
    user = cursor.fetchone()

    db.close()
    return user  # Will be None if no user found



@forgot_details_bp.route("/", methods=["GET", "POST"])
def forgot_details_page():
    if request.method == "POST":
        user_input = request.form.get('user_input')

        # Query DB for username or email
        user = get_user_by_username_or_email(user_input)

        # If user exists, send reset email
        # if user:
            # send_reset_email(user['email'])  # You implement this function

        # Always show the same message
        flash('You will shortly receive an email if your username or email exist. Please make sure to check your spam folder.', 'info')
        return redirect(url_for('forgot_details.forgot_details_page'))

    return render_template('forgot_details.html')
