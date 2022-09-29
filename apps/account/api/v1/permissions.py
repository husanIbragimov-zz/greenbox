from rest_framework import permissions


class IsOwnerOrReadOnlyForAccount(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.email == request.user.email


class IsAdminUserForAccount(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser and request.user.is_admin)


class IsAuthenticated(permissions.IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user or request.user.is_authenticated)
