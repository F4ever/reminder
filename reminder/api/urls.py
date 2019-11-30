from django.conf.urls import url

from api.views import NotificationViewSet, UserViewSet


urlpatterns = [
    # Users
    url(r'^users/$', UserViewSet.as_view({'get': 'list'})),

    # Notifications
    url(r'^notifications/$', NotificationViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^notifications/(?P<pk>[\d]+)/$', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'})),
]
