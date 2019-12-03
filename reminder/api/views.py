from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from api.serializers import UserProfileSerializer, NotificationSerializer
from api.utils import ReadOrOwnerPermission
from core.models import User
from notification.models import Notification


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ReadOrOwnerPermission]

    queryset = Notification.objects.prefetch_related('participators').order_by('date').distinct()
    serializer_class = NotificationSerializer

    filterset_fields = ['notified']

    def get_queryset(self):
        return self.queryset.filter(Q(creator=self.request.user) | Q(participators=self.request.user))

    def create(self, request, *args, **kwargs):
        request.data['creator'] = self.request.user.id
        return super().create(request, *args, **kwargs)
