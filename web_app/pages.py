from flask import Blueprint

bp = Blueprint("pages", __name__)

# Login page
@bp.route("/")
def home():
    return "Hello, Home!"

# Home screen
@bp.route("/home_screen")
def about():
    return

# Create new ticket screen
@bp.route("/add_ticket")
def about():
    return

# View existing tickets screen
@bp.route("/view_tickets")
def about():
    return

# Admin screen
@bp.route("/admin_screen")
def about():
    return

# Log out screen
@bp.route("/logout")
def about():
    return