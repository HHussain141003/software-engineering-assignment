from flask import Blueprint, render_template, session, redirect, url_for, flash, request, get_flashed_messages
from .database import get_db

view_individual_ticket_bp = Blueprint("view_individual_ticket", __name__)


@view_individual_ticket_bp.route("/view_tickets/<int:ticket_id>")
def view_ticket(ticket_id):
    db = get_db()
    user_id = session.get('user_id')
    role = session.get('role')

    # Admin can view all tickets
    if role == 'admin':
        ticket = db.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()
    else:
        # Regular users can only view their own tickets
        ticket = db.execute(
            'SELECT * FROM tickets WHERE id = ? AND user_id = ?',
            (ticket_id, user_id)
        ).fetchone()

    if not ticket:
        flash('Ticket not found or you do not have permission to view it!', 'danger')
        return redirect(url_for('view_tickets.view_tickets'))

    return render_template("view_ticket.html", ticket=ticket)