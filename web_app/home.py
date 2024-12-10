from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint("home", __name__)

@home_bp.route('/home', methods=['GET'])
def home_screen():
    return render_template('home_screen.html')

