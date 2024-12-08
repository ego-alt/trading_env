from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
celery_app = Celery("setup")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Schedule frequency and time period of different tasks
celery_app.conf.beat_schedule = {
    'log-asset-and-portfolio-history': {
        'task': 'trading_env.tasks.fetch_price_and_log_all_portfolio',
        'schedule': crontab(minute=0, hour=16), # Take a snapshot of portfolio value at 4pm every day
    },
}

