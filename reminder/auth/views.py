from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from auth.serializers import UserRegisterSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer


