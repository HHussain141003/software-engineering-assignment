from werkzeug.security import generate_password_hash
from . import get_db

def generate_user_data():
    db = get_db()
    users = [
        ('admin', 'admin@example.com', 'admin123', 'admin'),
        ('user1', 'user1@example.com', 'user1', 'user'),
        ('user2', 'user2@example.com', 'user2', 'user'),
        ('user3', 'user3@example.com', 'user3', 'user'),
        ('user4', 'user4@example.com', 'user4', 'user'),
        ('user5', 'user5@example.com', 'user5', 'user'),
        ('user6', 'user6@example.com', 'user6', 'user'),
        ('user7', 'user7@example.com', 'user7', 'user'),
        ('user8', 'user8@example.com', 'user8', 'user'),
        ('user9', 'user9@example.com', 'user9', 'user'),
    ]

    for username, email, password, role in users:
        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", (username, email, hashed_password, role))
        db.commit