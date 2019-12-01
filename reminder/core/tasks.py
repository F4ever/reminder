from django.conf import settings
from django.core.mail import send_mail

from reminder.celery import app


@app.task
def send_mail_task(head, body, to_emails):
    send_mail(
        subject=head,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=to_emails,
        fail_silently=False,
    )
