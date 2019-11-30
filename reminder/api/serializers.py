from rest_framework import serializers

from core.models import User
from notification.models import Notification


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username'
        )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id',
            'head',
            'body',
            'place',
            'date',
            'creator',
            'participators',
            'notified',
            'created_at',
        )
