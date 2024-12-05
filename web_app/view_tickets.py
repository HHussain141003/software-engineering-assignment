from flask import Blueprint, render_template, session, redirect, url_for
from .database import get_db

view_tickets_bp = Blueprint("view_tickets", __name__)

@view_tickets_bp.route("/view_tickets")
def view_tickets():
    user_id = session.get("user_id")

    db = get_db()
    tickets = db.execute(
        "SELECT id, title, description, status, priority, created_at FROM tickets WHERE user_id = ?",
        (user_id,)
    ).fetchall()

    return render_template("view_tickets.html", tickets=tickets)
