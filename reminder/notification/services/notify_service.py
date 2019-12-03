from core.tasks import send_mail_task


class NotifyService:
    def __init__(self, notification_query_set):
        # Some kind of optimization. So outside no need to know how it works inside
        self._notifications = notification_query_set.select_related('creator').prefetch_related('participators')

    def send_notifications(self):
        for notification in self._notifications.iterator():
            self._send_notification(notification)

        self._notifications.update(notified=True)

    def _send_notification(self, notification):
        to_emails = [user.email for user in notification.participators.all()]

        creator_email = notification.creator.email
        to_emails.append(creator_email)

        # send_mail is celery task, we do not want to wait until email will be send
        send_mail_task.delay(
            notification.head,
            notification.body,
            to_emails,
            details=f'Send notification with id: {notification.id}',
        )
