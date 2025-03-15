from rest_framework import permissions


class ActualUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.user == request.user


class NotActualUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user != obj.user
