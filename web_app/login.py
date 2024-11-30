from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from . import get_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    db = get_db()

    # Check username and password
    user = db.execute("SELECT * FROM users WHERE username = ?", (username)).fetchone()
    if user is None:
        flash("Invalid userrname or password, please try again.")
        return render_template("login.html")
        

