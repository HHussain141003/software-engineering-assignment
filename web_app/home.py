from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint("home", __name__)

@home_bp.route('/home', methods=['GET'])
def home_screen():
    return render_template('home_screen.html')

@home_bp.route('/add_ticket', methods=['GET'])
def create_ticket():
    return render_template('add_ticket.html')

@home_bp.route('/admin_screen', methods=['GET'])
def admin_screen():
    if session.get('role') == 'admin':
        return render_template('admin_screen.html')
