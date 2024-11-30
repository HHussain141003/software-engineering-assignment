from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

# Login page
@bp.route("/")
def login():
    return render_template("login.html")

# Home screen
@bp.route("/home_screen")
def home_screen():
    return "Home Screen"

# Create new ticket screen
@bp.route("/add_ticket")
def add_ticket():
    return "Add Ticket Screen"

# View existing tickets screen
@bp.route("/view_tickets")
def view_tickets():
    return "View Tickets Screen"

# Admin screen
@bp.route("/admin_screen")
def admin_screen():
    return "Admin Screen"

# Log out screen
@bp.route("/logout")
def logout():
    return "Logout Screen"
