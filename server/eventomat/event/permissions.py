from rest_framework import permissions


class KeyholderPermission(permissions.BasePermission):
    message = 'Only keyholders may edit data.'

    def has_permission(self, request, view):
        if request.resolver_match.url_name == 'event-attend' and request.method == 'POST':
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class OwnerDeletePermission(permissions.BasePermission):
    message = 'Only creator may delete event.'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user == obj.keyholder
        return True
