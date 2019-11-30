from django.conf.urls import url
from django.urls import path, include

from auth.views import UserRegisterViewSet, UserProfileViewSet

urlpatterns = [
    url(r'^me/$', UserProfileViewSet.as_view({'get': 'retrieve'})),
    url(r'^register/$', UserRegisterViewSet.as_view({'post': 'create'})),
    path(r'rest-auth/', include('rest_framework.urls')),
]
