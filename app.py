from flask import Flask, request, session, render_template
from dotenv import load_dotenv
import datetime

# import schedule_cron

load_dotenv()
from flask_debugtoolbar import DebugToolbarExtension
from crontab import CronTab
from flask_mail import Mail, Message
import os

from models import db, connect_db

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:////mnt/c/Users/trist/Documents/Springboard_Exercises/better-bets-skeleton/better_bets.db"
app.config["FLASK_ENV"] = os.environ.get("FLASK_ENV")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False


mail = Mail(app)

SQLALCHEMY_TRACK_MODIFICATIONS = True

connect_db(app)


@app.route("/test-email")
def send_test_email():
    msg = Message(
        "You're trash!",
        sender="cookiecancer93@gmail.com",
        recipients=["tristandavisbrody@gmail.com"],
    )
    msg.body = "Wow you're an idiot"
    mail.send(msg)
    return "tried to send something"
