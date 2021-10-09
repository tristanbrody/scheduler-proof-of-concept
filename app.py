from flask import Flask, request, session, render_template
from dotenv import load_dotenv
import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler


release_date = datetime.datetime(2021, 10, 17)
release_datetime = datetime(release_date.year, release_date.month, release_date.day)

first_time = datetime.datetime.now()
later_time = datetime.datetime.now()
difference = later_time - first_time
datetime.timedelta(0, 8, 562000)
seconds_in_day = 24 * 60 * 60
difference = divmod(difference.days * seconds_in_day + difference.seconds, 60)
final_difference = round(difference[0] / 60)
diff_as_str = str(final_difference)

# import schedule_cron

load_dotenv()
from flask_debugtoolbar import DebugToolbarExtension
from crontab import CronTab
from flask_mail import Mail, Message
import os

from models import db, connect_db

app = Flask(__name__)
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

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=60)
def timed_job():
    msg = Message(
        f"Succession drops in {diff_as_str} hours!",
        sender="cookiecancer93@gmail.com",
        recipients=[
            "brodyjackson775@gmail.com",
            "emmachinesepanda@gmail.com",
            "tristandavisbrody@gmail.com",
        ],
    )
    msg.body = "Wow you're an idiot"
    mail.send(msg)
    return "tried to send something"
