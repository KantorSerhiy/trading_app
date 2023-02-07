import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD

celery = Celery("tasks", broker="redis://localhost:6379")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def get_email_template(username: str):
    email = EmailMessage()
    email["Subject"] = "Trading"
    email["From"] = SMTP_USER
    email["To"] = SMTP_USER

    email.set_content(
        "<div>"
        f"<h1 style='color: red;'> Hello, {username}, here u report! Checkout</h1>"
        "</div>",
        subtype="html"
    )
    return email


@celery.task
def send_email_report(username: str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
