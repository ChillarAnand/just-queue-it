import random
import time

from celery import Celery, task


app = Celery(backend='amqp', broker='amqp://')


def run_task(n):
    try:
        time.sleep(2)
        number = random.randint(0, 9)
        if number in [2, 3]:
            raise Exception
        print("Task {0} Success".format(n))

    except Exception:
        print("Task {0} failed.....".format(n))


def run_tasks():
    for i in range(10):
        run_task(i)


@app.task(default_retry_delay=1 * 1)
def run_task_with_retry(n):
    try:
        time.sleep(2)
        number = random.randint(0, 9)
        if number in [2, 3]:
            raise Exception
        print("Task {0} Success".format(n))

    except Exception:
        print("Task {0} failed. Retrying...".format(n))
        raise task.current.retry()


def run_tasks_with_retry():
    for i in range(10):
        run_task_with_retry.delay(i)
