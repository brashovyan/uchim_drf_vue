from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()


class IsManufacturer(permissions.BasePermission):
    def has_permission(self, request, view):
        if User.objects.filter(pk=request.user.id, groups__name='Moderator').exists():
            return True
        else:
            return False