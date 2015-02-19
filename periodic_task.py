from datetime import timedelta

from celery import Celery
from celery.task import periodic_task


app = Celery('tasks', backend='amqp',
             broker='amqp://guest@localhost//')


@periodic_task(run_every=timedelta(seconds=4))
def sample():
    return 'Run every 4 seconds'
