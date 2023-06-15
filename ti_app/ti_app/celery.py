from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
import datetime
import os
from datetime import datetime
from django.conf import settings
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ti_app.settings')

app = Celery('ti_app')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Jerusalem')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-test-schedule': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': 20,  # Run the task every 20 seconds
        # 'schedule': crontab(hour=int((datetime.now()).hour), minute=int((datetime.now()).minute)+1)
        # 'args': (2,)
    }

}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
