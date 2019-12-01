import logging

from django.conf import settings
from django.core.mail import send_mail

from reminder.celery import app


logger = logging.getLogger(__name__)


@app.task
def send_mail_task(head, body, to_emails, details=''):
    try:
        send_mail(
            subject=head,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=to_emails,
            fail_silently=False,
        )
    except Exception as exp:
        logger.error(f'Can not send mail with exception: {exp}. Details: {details}')
        raise exp
