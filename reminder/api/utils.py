from rest_framework import permissions


class ReadOrOwnerPermission:
    def has_permission(self, request, view):
        """
        QuerySet is filtered in view, so here is no reason to check permissions
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        If it is owner of object (creator_id) then he can change it.
        Else if he is parcipicant he can only read it
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.creator == request.user:
            return True

        return False
