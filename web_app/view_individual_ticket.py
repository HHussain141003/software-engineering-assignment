from flask import Blueprint, render_template, session, redirect, url_for, flash, request, get_flashed_messages
from .database import get_db

view_individual_ticket_bp = Blueprint("view_individual_ticket", __name__)


@view_individual_ticket_bp.route("/view_tickets/<int:ticket_id>")
def view_ticket(ticket_id):
    db = get_db()
    user_id = session.get('user_id')
    role = session.get('role')

    ticket = db.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()

    if not ticket:
        flash('Ticket not found or you do not have permission to view it!', 'error')
        return redirect(url_for('view_tickets.view_tickets'))

    prev_page = request.args.get('prev_page', None)

    if not prev_page:
        prev_page = session.get('prev_page', url_for('home.home_screen'))

    session['prev_page'] = request.referrer or url_for('home.home_screen')
    return render_template("view_ticket.html", ticket=ticket, prev_page=prev_page)