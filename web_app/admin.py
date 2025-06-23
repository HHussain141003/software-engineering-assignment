from flask import Blueprint, render_template, request, flash, redirect, url_for, session, get_flashed_messages
from datetime import datetime
from .database import get_db
from werkzeug.security import generate_password_hash
from urllib.parse import unquote
import re

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
    prev_page = request.args.get('prev_page', session.get('prev_page', url_for('home.home_screen')))
    prev_page = unquote(prev_page)  # URL decode to ensure proper handling of the URL

    session['prev_page'] = request.referrer or url_for('home.home_screen')

    # Process the form if it's a POST request
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
    
    # Retrieve ticket information for editing
    ticket = db.execute('SELECT * FROM tickets WHERE id = ?',(ticket_id,)).fetchone()

    # Pass the ticket data and prev_page to the template
    return render_template('edit_ticket.html', ticket=ticket, prev_page=prev_page)

def is_strong_password(password):
    # At least 8 characters, 1 lowercase, 1 uppercase, 1 digit, 1 special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.match(pattern, password)

@admin_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        if not is_strong_password(password):
            flash("Password must be at least 8 characters long and include 1 lowercase, 1 uppercase, 1 digit, and 1 special character.", "error")
            return redirect(url_for("admin_bp.add_user"))

        db = get_db()
        existing_user = db.execute(
            "SELECT * FROM users WHERE username = ? OR email = ?", (username, email)
        ).fetchone()
        if existing_user:
            flash("Username or email already exists. Please use another.", "error")
            return redirect(url_for("admin_bp.add_user"))

        hashed_password = generate_password_hash(password)
        db.execute(
            "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
            (username, email, hashed_password, role),
        )
        db.commit()

        flash("New user added successfully!", "user_added")
        return redirect(url_for("admin_bp.add_user"))

    return render_template("add_user.html")