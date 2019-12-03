from django.contrib import admin

from notification.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    show_full_result_count = False
    raw_id_fields = ('participators', 'creator')


admin.site.register(Notification, NotificationAdmin)
