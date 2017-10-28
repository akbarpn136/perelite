from django.contrib.auth import hashers
# from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse
from rest_framework import generics
from . import models
from .helpers import (create_exception,
                      retrieve_exception,
                      generate_key,
                      check_instance)
from .paginations import Pagination


class Personil(generics.ListCreateAPIView):
    def get_queryset(self):
        personil = Pagination(self.request.GET, models.Personil.objects)

        return personil.paginate()

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.get_queryset())

    def post(self, request, *args, **kwargs):
        personil = models.Personil(
            username=request.POST.get('username'),
            password=hashers.make_password(request.POST.get('password')),
            token=generate_key(),
            nama_depan=request.POST.get('nama_depan'),
            nama_belakang=request.POST.get('nama_belakang'),
            email=request.POST.get('email')
        )

        return create_exception(personil)


class PersonilModifikasi(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return retrieve_exception(models.Personil.objects.get(username=self.kwargs['username']))

    def get(self, request, *args, **kwargs):
        return check_instance(self.get_object(), models.Personil)

    def put(self, request, *args, **kwargs):
        return check_instance(self.get_object(), models.Personil)

    def delete(self, request, *args, **kwargs):
        return check_instance(self.get_object(), models.Personil, self.get_object().delete())
