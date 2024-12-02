from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

# Login page
@bp.route("/")
def login():
    return render_template("login.html")

# Home screen
@bp.route("/home_screen")
def home_screen():
    return render_template("home_screen.html")

# Create new ticket screen
@bp.route("/add_ticket")
def add_ticket():
    return render_template("add_ticket.html")

# View existing tickets screen
@bp.route("/view_tickets")
def view_tickets():
    return render_template("view_tickets.html")

# Admin screen
@bp.route("/admin_screen")
def admin_screen():
    return render_template("admin_screen.html")

# Log out screen
@bp.route("/logout")
def logout():
    return render_template("logout.html")
