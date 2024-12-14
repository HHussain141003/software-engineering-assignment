# Table of Contents

- [Introduction](#introduction)
  - [Problem Statement](#problem-statement)
  - [Project Scope Statement](#scope-statement)
- [Setting up the Application](#setting-up-the-application)
- [App Use](#app-use)
  - [Log-in](#log-in)

# Introduction

(**Note:** This is a fictional scenario for educational purposes)

## Problem Statement

1. **Problem:** Fujitsu employees do not have an efficient system in place to raise support tickets with IT Helpdesk raising inefficiencies in tracking and solving the issues.

2. **Background:** Fujitsu does not have a process that allows employees to request support for common issues with their devices. Communication is primarily done through Microsoft Teams or Microsoft Outlook, this causes frequent delays and miscommunication, which makes the IT Helpdesk inconsistent.

3. **Relevance:** Inefficient ticket management can lead to slow resolution of issues, decreasing employees productivity as their operations are disrupted. The inconvenience of the ticket management system can also reduce user satisfaction leading to decreased morale and productivity.

4. **Objectives:** This project aims to develop a web based IT Support Ticket Management System using Flask, SQLite, and Python. The application will include features for Creating, Updating, and Managing support tickets, with role-based access controls for users and administrators. This project aims to streamline the ticket management system and provide improved resolution times, enhance user satisfaction, and create a knowledgebase with the record details being used for future training.

## Scope Statement

1. **Project Name:** IT Support Ticket Management System.

2. **Scope Overview:** This project focuses on delivering a web based IT Support Ticket Management System to improve ticket resolution. The system will provide a user friendly interface for both **users** and **administrators** allowing effective ticket creation, update, and tracking.

3. **In Scope:**

   - User Authentication and Authorization for 2 users:

     - Basic User: Limited CRUD operations (Excluding Update and Delete)

     - Administrator: Full CRUD operations (Excluding Delete)

   - Ticket management features:

     - Creation, update, and viewing of support request tickets.

     - Validation to ensure accurate and consistent support request tickets.

     - Tickets cannot be explicitly deleted since they can still be used to identify recurring tickets, trends, or patterns which might be adversely affected if tickets are deleted. However they can be marked as Cancelled or Resolved to "soft delete" them.

   - Comments:

     - Users can add comments to the tickets to record a conversation and information associated with the issue.

     - Administrators can view and respond to comments made on any support request ticket.

   - Database Integration:

     - Implementation of an SQLite database to store user information, tickets, and comments.

     - Relationship between the tables to ensure daa integrity.

   - Code and Documentation:

     - Modularized and clean code that adheres to industry standards.

     - Comprehensive documentation with setup and usage instructions.

     - Annotated screenshots of the running application.

4. **Out of scope:**

   - Integrations with third party systems.

   - Real-Time notifications (e.g. Email or Message alerts).

   - Advanced analytics or reporting tools for ticket trends and patterns.

5. **Assumptions:**

   - The system will be run locally, all the code is hosted in this repository.

   - Users will have access to the internet and a browser to use the system.

   - Initial test data (10 records for each table) will be automatically generated for demonstration purposes.

6. **Constraints:**

   - The system will utilize SQLite which is a small scale database suitable for small-scale operations.

   - The styling of the application will be basic since the academic requirements do not grant marks for design or UX.

# Setting up the Application

- Create a virtual environment: `python -m venv venv`

- Install dependencies: `pip install -r requirements.txt`

- Create a `.env` file and add any value e.g. `SECRET_KEY = 'flask_secret_key_123'`

# App Use:

## Log-in

There are 10 user records generated automatically. There are 9 users and 1 admin. The details are as follow:

- User:

```
username: user1
password: user1
```

- Admin:

```
username: admin
password: admin123
```

# App Documentation:

This app aims to simulate an IT Support app where a user can raise a ticked and an IT Support officer will aim to resolve them. There are 3 tables, User, Ticket, and Comment

## Entity Relationship Diagram:

![ERD](./documentation/erd.png)
