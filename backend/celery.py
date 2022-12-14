import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

celery = Celery('backend')
celery.config_from_object('django.conf:settings', namespace='CELERY')
#celery.autodiscover_tasks()
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
