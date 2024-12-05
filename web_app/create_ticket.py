from flask import Blueprint, render_template, session, redirect, url_for, flash

create_ticket = Blueprint("create_ticket", __name__)

# @create_ticket.route("/create_ticket")
# def 