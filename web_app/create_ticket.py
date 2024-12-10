from flask import Blueprint, render_template, session, redirect, url_for, flash, request, get_flashed_messages
from datetime import datetime
from .database import get_db

create_ticket_bp = Blueprint("create_ticket", __name__)

@create_ticket_bp.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
    if request.method == "POST":
        user_id = session.get("user_id")
        title = request.form["title"]
        description = request.form['description']
        priority = request.form['priority']
        status = 'Created'
        created_at = updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        db = get_db()

        db.execute(
            'INSERT INTO tickets (title, description, status, priority, created_at, updated_at, user_id) '
            'VALUES (?, ?, ?, ?, ?, ?, ?)',
            (title, description, status, priority, created_at, updated_at, user_id)
        )

        db.commit()

        ticket_id = db.execute('SELECT last_insert_rowid()').fetchone()[0]

        flash('Ticket created successfully!', 'create_ticket_message')
        return redirect(url_for('view_individual_ticket.view_ticket', ticket_id=ticket_id))

    return render_template('create_ticket.html', ticket="", description="", priority="Low", status="Created", created_at="", updated_at="")

