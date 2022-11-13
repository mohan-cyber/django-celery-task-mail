from celery import shared_task, current_task

from apps.mail.utils import Utils

@shared_task(name="send_welcome_email")
def send_email(email, data):
    print("hello world")
    return Utils.send_welcome_mail(email, data)
