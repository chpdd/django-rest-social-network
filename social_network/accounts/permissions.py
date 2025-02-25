from rest_framework import permissions


class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


class IsUserOrClose(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj
