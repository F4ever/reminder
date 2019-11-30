import logging

from notification.tasks import send_mail

logger = logging.getLogger(__name__)


class NotifyService:
    def __init__(self, notification_query_set):
        # Some kind of optimization. So outside no need to know how it works inside
        self._notifications = notification_query_set.select_related('creator').prefetch_related('participators')

    def send_notifications(self):
        for notification in self._notifications.iterator():
            self._send_notification(notification)

    def _send_notification(self, notification):
        to_emails = [user.email for user in notification.participators.all()]

        creator_email = notification.creator.email
        to_emails.append(creator_email)

        try:
            # send_mail is celery task, we do not want to wait until email will be send
            send_mail(
                notification.head,
                notification.body,
                to_emails,
            )
        except Exception as exp:
            # Return without changing notification status and log the error
            logger.error(f'Can not send notification with id: {notification.id} with exception: {exp}')
            return

        notification.notified = True
        notification.save(update_fields=['notified'])

