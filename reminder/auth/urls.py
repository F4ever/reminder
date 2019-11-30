from django.conf.urls import url

from auth.views import UserProfileViewSet, UserAuthViewSet


urlpatterns = [
    url(r'^me/$', UserProfileViewSet.as_view({'get': 'retrieve'})),
    url(r'^register/$', UserAuthViewSet.as_view({'post': 'register'})),
    url(r'^login/$', UserAuthViewSet.as_view({'post': 'login'})),
    url(r'^logout/$', UserAuthViewSet.as_view({'post': 'logout'})),
]
