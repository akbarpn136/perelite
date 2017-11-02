import json
from django.contrib.auth import hashers
# from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse
from rest_framework import generics
from . import models
from .helpers import (create_exception,
                      generate_key,
                      check_instance)
from .paginations import Pagination
from mongoengine import errors


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
        try:
            return models.Personil.objects.get(username=self.kwargs['username'])

        except models.Personil.DoesNotExist:
            return json.dumps({
                'detail': 'Matching query does not exist.'
            })

        except models.Personil.MultipleObjectsReturned:
            return json.dumps({
                'detail': 'Document not unique.'
            })

    def get(self, request, *args, **kwargs):
        return check_instance(self.get_object(),
                              models.Personil)

    def put(self, request, *args, **kwargs):
        def execute():
            try:
                return self.get_object().update(
                    set__nama_depan=request.POST.get('nama_depan'),
                    set__nama_belakang=request.POST.get('nama_belakang'),
                    set__super=bool(request.POST.get('super')),
                    set__email=request.POST.get('email')
                )

            except errors.ValidationError as err:
                return json.dumps({
                    'detail': err.message
                })

        return check_instance(self.get_object(),
                              models.Personil,
                              execute())

    def delete(self, request, *args, **kwargs):
        def execute():
            return self.get_object().delete()

        return check_instance(self.get_object(),
                              models.Personil,
                              execute())
