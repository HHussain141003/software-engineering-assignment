from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from .database import get_db

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin_view_all_tickets')
def admin_view_all_tickets():
    db = get_db()
    tickets = db.execute(
        '''
        SELECT tickets.*, users.username
        FROM tickets
        JOIN users ON tickets.user_id = users.id
        '''
    ).fetchall()

    return render_template('admin_screen.html', tickets=tickets)

@admin_bp.route('/edit_ticket/<int:ticket_id>', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    db = get_db()

    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        status = request.form['status']
        updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        db.execute(
            '''
            UPDATE tickets
            SET title = ?, description = ?, priority = ?, status = ?, updated_at = ?
            WHERE id = ?
            ''',
            (title, description, priority, status, updated_at, ticket_id)
        )

        db.commit()
        flash('Ticket updated successfully!', 'success')
        return redirect(url_for('admin_bp.admin_view_all_tickets'))
    
    ticket = db.execute('SELECT * FROM tickets WHERE id = ?',(ticket_id,)).fetchone()

    return render_template('edit_ticket.html', ticket=ticket)