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
    status TEXT NOT NULL DEFAULT 'Open',
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

-- Sample data for each table
INSERT INTO tickets (title, description, status, priority, user_id) VALUES
('Login Issue', 'User cannot log in to their account.', 'Open', 'High', 2),
('Broken Printer', 'The office printer is not working.', 'Open', 'Medium', 3),
('Software Request', 'Request for Adobe Photoshop license.', 'Open', 'Low', 4),
('System Crash', 'The computer crashed during work.', 'In Progress', 'High', 5),
('Email Issue', 'Unable to send emails.', 'Resolved', 'High', 6),
('Network Problem', 'Internet connection is unstable.', 'Open', 'Medium', 7),
('Access Denied', 'Cannot access shared folder.', 'In Progress', 'Low', 8),
('Update Error', 'System update failed to install.', 'Open', 'High', 9),
('Slow Performance', 'Computer is running very slow.', 'Resolved', 'Medium', 10),
('Hardware Issue', 'Mouse is not functioning properly.', 'Open', 'Low', 2);

INSERT INTO comments (ticket_id, user_id, comment) VALUES
(1, 3, 'Have you tried resetting your password?'),
(1, 2, 'Yes, but the problem persists.'),
(2, 5, 'Contacted the printer vendor for support.'),
(3, 4, 'License request submitted to the IT department.'),
(4, 6, 'The crash logs have been reviewed, reinstalling drivers.'),
(5, 7, 'Issue resolved after email settings were corrected.'),
(6, 8, 'Network cables checked, awaiting ISP response.'),
(7, 9, 'Permission issue identified, working on resolution.'),
(8, 10, 'Retrying the update with the correct installer.'),
(9, 2, 'Cleared cache and ran diagnostics, system improved.');