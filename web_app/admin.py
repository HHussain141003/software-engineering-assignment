from flask import Blueprint, render_template
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
