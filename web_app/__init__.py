from flask import Flask
import os
import logging
from .pages import bp
from .login import login_bp
from .database import get_db
from .data import generate_user_data
from dotenv import load_dotenv

load_dotenv

secret_key = os.getenv("SECRET_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_app():

    template_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "templates")
    )

    app = Flask(__name__, template_folder=template_folder_path)

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
        else:
            logger.info("Database found")

    initialize_database()
    generate_user_data()
    app.secret_key = secret_key
    app.register_blueprint(bp)
    app.register_blueprint(login_bp)

    return app