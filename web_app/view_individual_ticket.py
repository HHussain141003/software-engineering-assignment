from flask import Blueprint, render_template, session, redirect, url_for, flash, request, get_flashed_messages
from .database import get_db

view_individual_ticket_bp = Blueprint("view_individual_ticket", __name__)


@view_individual_ticket_bp.route("/view_tickets/<int:ticket_id>", methods=["GET", "POST"])
def view_ticket(ticket_id):
    db = get_db()
    user_id = session.get('user_id')
    role = session.get('role')

    ticket = db.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()

    if not ticket:
        flash('Ticket not found or you do not have permission to view it!', 'error')
        return redirect(url_for('view_tickets.view_tickets'))

    comments = db.execute(
        '''
        SELECT c.comment, c.created_at, u.username 
        FROM comments c 
        JOIN users u ON c.user_id = u.id 
        WHERE c.ticket_id = ? 
        ORDER BY c.created_at ASC
        ''', 
        (ticket_id,)
    ).fetchall()

    if request.method == "POST":
        content = request.form.get("content")
        if not content:
            flash("Comment cannot be empty!", "error")
        else:
            db.execute(
                'INSERT INTO comments (ticket_id, user_id, comment) VALUES (?, ?, ?)',
                (ticket_id, user_id, content)
            )
            db.commit()
            flash("Comment added successfully!", "success")
            return redirect(url_for('view_individual_ticket.view_ticket', ticket_id=ticket_id))

    prev_page = request.args.get('prev_page', session.get('prev_page', url_for('home.home_screen')))
    session['prev_page'] = request.referrer or url_for('home.home_screen')

    return render_template("view_ticket.html", ticket=ticket, comments=comments, prev_page=prev_page)
