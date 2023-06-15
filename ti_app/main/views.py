from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def authorization(request):
    return HttpResponse("<h4>authorization</h4>")


def info(request):
    return HttpResponse("<h4>info</h4>")


