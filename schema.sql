DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS comments;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user'
);

CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Created',
    priority TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    comment TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Sample data for each table (Sample data for user table is in data.py since the passwords require encryption.)
INSERT INTO tickets (title, description, status, priority, user_id) VALUES
('Login Issue', 'Unable to log in to account.', 'On hold', 'High', 2),
('Broken Printer', 'The office printer is not working.', 'In progress', 'Medium', 3),
('Software Request', 'Request for Adobe Photoshop license.', 'On hold', 'Low', 4),
('System Crash', 'Computer crashed unexpectedly.', 'In Progress', 'High', 5),
('Email Issue', 'Unable to send and receive emails.', 'Resolved', 'High', 6),
('Network Problem', 'Internet connection drops frequently.', 'On hold', 'Medium', 7),
('Access Denied', 'No access to the shared folder.', 'In Progress', 'Low', 8),
('Update Error', 'System update failed repeatedly.', 'In Progress', 'High', 9),
('Slow Performance', 'System is very slow to respond.', 'Resolved', 'Medium', 10),
('Hardware Issue', 'Mouse is not functioning properly.', 'Created', 'Low', 2);

INSERT INTO comments (ticket_id, user_id, comment) VALUES
(1, 2, 'I tried resetting the password, but it did not work.'),
(2, 3, 'Contacted printer vendor for assistance.'),
(3, 4, 'I submitted the license request to the IT team.'),
(4, 5, 'Reinstalled drivers and monitored for stability.'),
(5, 6, 'Resolved after correcting the email server settings.'),
(6, 7, 'Checked the cables, waiting for ISP update.'),
(7, 8, 'It appears to be a permission issue, fixing now.'),
(8, 9, 'Attempting update with proper installer settings.'),
(9, 10, 'Ran diagnostics and cleaned unnecessary files.'),
(10, 2, 'Replaced the mouse, now functioning properly.');