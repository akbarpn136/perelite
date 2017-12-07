from rest_framework import exceptions
from rest_framework import permissions
from . import models
from perelite_core import models


def _user(username):
    return models.Personil.objects.get(username=username)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return _user(request.user.username).is_superuser()

        except models.Personil.DoesNotExist:
            raise exceptions.PermissionDenied()


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return _user(request.user.username).is_authenticated()

        except models.Personil.DoesNotExist:
            raise exceptions.PermissionDenied()


class IsOwnerTugas(permissions.BasePermission):
    def has_permission(self, request, view):
        tugas = getattr(view, 'tugas')

        try:
            return tugas.owner.username == request.user.username

        except models.Tugas.DoesNotExist:
            raise exceptions.PermissionDenied()


class IsAdminOrLimitedAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if _user(request.user.username).is_superuser():
                return True
            else:
                return True if request.method == 'GET' else False

        except models.Personil.DoesNotExist:
            raise exceptions.PermissionDenied()
