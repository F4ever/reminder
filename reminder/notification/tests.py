import pytz
from django.test import TestCase
from faker import Faker

from core.models import User
from notification.models import Notification
from notification.services.notify_service import NotifyService


class NotificationServiceTest(TestCase):
    """
    Testing our service
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user = User.objects.create(email='some@email.com')

        fake = Faker()

        notifications = []

        for i in range(10):
            notification = Notification(
                head='Mail head',
                body='Mail body',
                place='Fake place',
                date=fake.future_datetime(end_date='+1d', tzinfo=pytz.UTC),
                creator=user,
            )
            notifications.append(notification)

        Notification.objects.bulk_create(notifications)

    def test_notification_send(self):
        notifications = Notification.objects.all()

        assert Notification.objects.filter(notified=False).count() == 10

        notify_service = NotifyService(notification_query_set=notifications)
        notify_service.send_notifications()

        assert Notification.objects.filter(notified=False).count() == 0
