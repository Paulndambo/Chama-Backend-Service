from backend.celery import celery
from celery import shared_task


celery.conf.beat_schedule = {
    'run-every-2-seconds': {
        'task': 'say_hello',
        'schedule': 2,
        'args': ['Hello World']
    }
}
