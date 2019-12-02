import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.template.loader import get_template
from django.template.response import SimpleTemplateResponse
from django.urls import path, include


urlpatterns = [
    # Auth endpoints
    path(r'auth-api/', include('auth.urls')),

    # Notification endpoints
    path(r'api/v1/', include('api.urls')),

    # Django admin
    path(r'admin/', admin.site.urls),

    # Django debugtoolbar
    url(r'^__debug__/', include(debug_toolbar.urls)),

    # Frontend
    url(r'^', lambda request: SimpleTemplateResponse(get_template('index.html'))),
]
