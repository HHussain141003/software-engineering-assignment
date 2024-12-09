from flask import Blueprint, render_template, session, redirect, url_for, flash, request, get_flashed_messages
from datetime import datetime
from .database import get_db

view_individual_ticket_bp = Blueprint("view_individual_ticket", __name__)


@view_individual_ticket_bp.route("/view_tickets/<int:ticket_id>")
def view_ticket(ticket_id):
    db = get_db()

    ticket = db.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()

    if not ticket:
        flash('Ticket not found!', 'danger')
        return redirect(url_for('create_ticket.create_ticket'))
    
    return render_template("view_ticket.html", ticket=ticket)