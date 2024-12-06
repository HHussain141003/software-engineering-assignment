from flask import Blueprint, render_template, session, redirect, url_for, flash, request
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

        flash('Ticket created successfully!', 'success')
        return render_template(
            'create_ticket.html',
            created_at=created_at,
            updated_at=updated_at,
            title=title,
            description=description,
            priority=priority,
            status=status
        )

    return render_template('create_ticket.html')