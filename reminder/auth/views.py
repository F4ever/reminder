from django.contrib.auth import login, authenticate, logout
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth.serializers import UserRegisterSerializer, UserProfileSerializer, UserLoginSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class UserAuthViewSet(viewsets.ViewSet):
    def register(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        login(request, user)

        return Response(status=status.HTTP_201_CREATED, data=UserProfileSerializer(user).data)

    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK, data=UserProfileSerializer(user).data)
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': 'The email address or password is incorrect'},
            )

    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)