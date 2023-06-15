from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta


@shared_task(bind=True)
def send_mail_func(self):
    send_mail('mail under celery',
              'Celery is cool',
              'pavel87.test@gmail.com',
              ['dolliner.pavel@gmail.com']
              )
    return "Done"
