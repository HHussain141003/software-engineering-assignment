from flask import Flask, request, session, flash, redirect, url_for
import os
import logging
from .login import login_bp
from .home import home_bp
from .database import get_db
from .data import generate_user_data
from .view_tickets import view_tickets_bp
from .create_ticket import create_ticket_bp
from dotenv import load_dotenv
from .functions import login_required
from .view_individual_ticket import view_individual_ticket_bp
from .admin import admin_bp
from .forgot_details import forgot_details_bp
load_dotenv

secret_key = os.getenv("SECRET_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_app():
    # Need to declare paths manually (both for Templates and Static)
    template_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "templates")
    )

    static_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "static")
    )

    app = Flask(__name__, template_folder=template_folder_path, static_folder=static_folder_path)

    @app.before_request
    def initialize_database():

        db_path = os.path.join(os.path.dirname(__file__), "database.db")

        if not os.path.exists(db_path):
            logger.info("Database does not exist, creating a new database.")

            schema_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "schema.sql")
            )

            with app.open_resource(schema_path) as f:
                db = get_db()
                db.executescript(f.read().decode("utf8"))
                db.commit()
            logger.info("New database created")

    @app.before_request
    def require_login():
        public_prefixes = ("login", "forgot_details", "static")
        if request.endpoint:
            if not request.endpoint.startswith(public_prefixes) and 'user_id' not in session:
                flash("You must be logged in to access this page.", "error")
                return redirect(url_for('login.login'))
        
    initialize_database()
    generate_user_data()
    app.secret_key = secret_key
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(view_tickets_bp)
    app.register_blueprint(create_ticket_bp)
    app.register_blueprint(view_individual_ticket_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(forgot_details_bp)

    return app 