DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

INSERT INTO users (username, email, password) VALUES ('admin', 'admin@example.com', 'admin123');
INSERT INTO users (username, email, password) VALUES ('user1', 'user1@example.com', 'user123');