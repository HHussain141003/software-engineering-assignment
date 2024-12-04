from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint("home", __name__)

@home_bp.route('/add_ticket', methods=['GET'])
def create_ticket():
    return render_template('add_ticket.html')

def view_tickets():
    return render_template('view_tickets.html')

def admin_screen():
    if session.get('role') == 'admin':
        return render_template('add_ticket.html')