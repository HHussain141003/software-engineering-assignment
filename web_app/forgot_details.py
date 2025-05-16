from flask import Blueprint, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from .database import get_db
import logging
import sqlite3
import smtplib
import requests
import os
from dotenv import load_dotenv
from itsdangerous import URLSafeTimedSerializer

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

forgot_details_bp = Blueprint("forgot_details", __name__, url_prefix='/forgot')

def generate_reset_token(email):
    secret_key = os.getenv("SECRET_KEY")
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(email, salt="reset-password")

def get_user_by_username_or_email(user_input):
    db = get_db()
    db.row_factory = sqlite3.Row 
    cursor = db.cursor()

    query = '''
    SELECT * FROM users
    WHERE username = ? OR email = ?
    '''
    cursor.execute(query, (user_input, user_input))
    user = cursor.fetchone()

    db.close()
    return user  # Will be None if no user found

def send_reset_email(recipient_email, username):
    token = generate_reset_token(recipient_email)
    reset_url = url_for("forgot_details.reset_password", token=token, _external=True)
    api_key = os.getenv("EMAIL_API_KEY")
    sender_email = "hhussain141003@gmail.com" 

    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }

    subject = "Password Reset Request"
    body = f"""
    Hello {username},

    We received a request to reset your password. 
    If this was you, please follow the instructions.

    If you did not request this, you can safely ignore this email.

    Thank you,

    Fujitsu IT Support Team
    """

    payload = {
        "sender": {"email": sender_email, "name": "IT Support Team"},
        "to": [{"email": recipient_email}],
        "subject": subject,
        "textContent": body
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        logger.info(f"Password reset email sent to {recipient_email}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send email: {e}")

@forgot_details_bp.route("/", methods=["GET", "POST"])
def forgot_details_page():
    if request.method == "POST":
        user_input = request.form.get('user_input')

        # Query DB for username or email
        user = get_user_by_username_or_email(user_input)

        if user:
            send_reset_email(user['email'], user['username'])

        flash('You will shortly receive an email if your username or email exist. Please make sure to check your spam folder.', 'info')
        return redirect(url_for('forgot_details.forgot_details_page'))

    return render_template('forgot_details.html')
