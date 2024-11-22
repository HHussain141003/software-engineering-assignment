from flask import Flask
from .pages import bp
import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row 
    return conn

def initialize_app():
    app = Flask(__name__)

    @app.before_request
    def initialize_database():
        with app.open_resource("..\schema.sql") as f:
            db = get_db()
            db.executescript(f.read().decode("utf8"))
            db.commit()
    app.register_blueprint(bp)
    return app