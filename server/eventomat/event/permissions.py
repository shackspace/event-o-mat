from rest_framework import permissions


class KeyholderPermission(permissions.BasePermission):
    message = 'Only keyholders may edit data.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
