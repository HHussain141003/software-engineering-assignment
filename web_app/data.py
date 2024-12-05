from werkzeug.security import generate_password_hash
from .database import get_db

def generate_user_data():
    db = get_db()

    existing_users = db.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if existing_users > 0:
        print("Sample data already exists.")
        return

    users = [
        (1,'admin', 'admin@example.com', 'admin123', 'admin'),
        (2,'user1', 'user1@example.com', 'user1', 'user'),
        (3,'user2', 'user2@example.com', 'user2', 'user'),
        (4,'user3', 'user3@example.com', 'user3', 'user'),
        (5,'user4', 'user4@example.com', 'user4', 'user'),
        (6,'user5', 'user5@example.com', 'user5', 'user'),
        (7,'user6', 'user6@example.com', 'user6', 'user'),
        (8,'user7', 'user7@example.com', 'user7', 'user'),
        (9,'user8', 'user8@example.com', 'user8', 'user'),
        (10,'user9', 'user9@example.com', 'user9', 'user'),
    ]

    for id, username, email, password, role in users:
        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO users (id, username, email, password, role) VALUES (?, ?, ?, ?, ?)", (id, username, email, hashed_password, role))
    
    db.commit()