from backend.celery import celery
from celery import shared_task

@celery.task(name='say_hello')
def say_hello(message):
    print(message)


