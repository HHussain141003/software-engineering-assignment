from flask import Flask
from .pages import bp
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row 
    return conn

def initialize_app():
    app = Flask(__name__)

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
    app.register_blueprint(bp)
    return app