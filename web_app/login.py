from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .database import get_db
import logging
from werkzeug.security import check_password_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    db = get_db()

    # Check username and password
    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if user is None:
        flash("Invalid username or password, please try again.")
        return render_template("login.html")
    
    if not check_password_hash(user["password"], password):
        flash("Invalid username or password, please try again.")
        return render_template("login.html")

    session["user_id"] = user["id"]
    session["role"] = user["role"]
    flash("Successfully logged in")
    return redirect(url_for("pages.home_screen"))