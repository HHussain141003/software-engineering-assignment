from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from .database import get_db
from werkzeug.security import generate_password_hash

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

@admin_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

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

        flash("New user added successfully!", "success")
        return redirect(url_for("admin_bp.add_user"))

    return render_template("add_user.html")