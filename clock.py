from app import app
from app import sched
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=60)
def timed_job():
    with app.app_context():
        msg = Message(
            f"Succession drops in {diff_as_str} hours!",
            sender="cookiecancer93@gmail.com",
            recipients=[
                "tristandavisbrody@gmail.com",
            ],
        )
        msg.body = "Boar on the floor!"
        mail.send(msg)
    return "tried to send something"


sched.start()
