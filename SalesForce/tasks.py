from django.dispatch import Signal

from celery.decorators import periodic_task
from celery.task.schedules import crontab
from .models import *
from .utlis import *

from datetime import timedelta  ,datetime 
from celery import task , shared_task

@periodic_task(run_every = timedelta(hours=1))
def refresh_access_token():
	new_obj = new_access_token()


