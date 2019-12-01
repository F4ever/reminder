import datetime

from notification.models import Notification
from notification.services.notify_service import NotifyService
from reminder.celery import app


@app.task
def send_actual_notifications():
    today = datetime.datetime.now()

    actual_notifications = Notification.objects.filter(
        date__year=today.year,
        date__month=today.month,
        date__day=today.day,
        date__hour=today.hour,
        date__minute=today.minute,
    )

    notify_service = NotifyService(notification_query_set=actual_notifications)
    notify_service.send_notifications()
