from django.db import models


class Notification(models.Model):
    # The recommendation for no more than 78 characters in the subject header
    head = models.CharField(max_length=78)
    body = models.TextField()
    place = models.CharField(max_length=256)
    date = models.DateTimeField()

    creator = models.ForeignKey('core.User', on_delete=models.CASCADE)
    participators = models.ManyToManyField('core.User', related_name='notifications')

    notified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification: {self.id}. Created at: {self.created_at}'
