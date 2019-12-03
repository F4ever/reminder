from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder.settings')

app = Celery('reminder')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notifications': {
        'task': 'notification.tasks.send_actual_notifications',
        'schedule': crontab(),  # execute every minute
    },
}

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'send_notifications': {
            'task': 'notification.tasks.send_actual_notifications',
            'schedule': timedelta(minutes=1),
        }
    }
)