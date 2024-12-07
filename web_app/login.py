from flask import Blueprint, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from .database import get_db
import logging
from werkzeug.security import check_password_hash
from .home import home_bp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["GET","POST"])
def login():
    # message_reset = get_flashed_messages()
    if request.method == "POST":
        return login_user()
    return render_template("login.html")

def login_user():
    username = request.form["username"]
    password = request.form["password"]

    db = get_db()

    # Check username and password
    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if user is None:
        flash("Invalid username or password, please try again.", "login_status")
        return render_template("login.html")
    
    if not check_password_hash(user["password"], password):
        flash("Invalid username or password, please try again.", "login_status")
        return render_template("login.html")

    session["user_id"] = user["id"]
    session["role"] = user["role"]
    flash("Successfully logged in", "login_status")
    return redirect(url_for("home.home_screen"))

@login_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect(url_for('login.login'))