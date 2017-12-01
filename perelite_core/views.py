from django.http import HttpResponse
from rest_framework import generics
from rest_framework import exceptions
from . import models
from perelite_utility import permissions, paginations


class Tugas(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminOrLimitedAuthenticated,)

    def get_queryset(self):
        tugas = paginations.Pagination(self.request.GET, models.Tugas.objects)

        return tugas.paginate()

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.get_queryset())
