from django.http import HttpResponse
from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

from .tasks import *


def index(request):
    # Set a delay of 10 seconds for the task at the point of calling

    #send_mail_func()
    bar()
#    send_mail_without_celery()

    return HttpResponse("<h1>Hello ,</h1>")


#def test(request):
#    test_func.delay()
#    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")
