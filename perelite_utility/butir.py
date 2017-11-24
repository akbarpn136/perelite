import json
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import exceptions
from . import models
from . import permissions
from .helpers import (create_exception, check_instance)
from .paginations import Pagination
from mongoengine import errors


# Create your views here.
class Butir(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminOrLimitedAuthenticated,)

    def get_queryset(self):
        kategori = self.kwargs.get('kategori')
        query = models.Butir
        if kategori == 'pendidikan':
            query = query.objects(butir__startswith='I.')
        elif kategori == 'kerekayasaan':
            query = query.objects(butir__startswith='II.')
        elif kategori == 'profesi':
            query = query.objects(butir__startswith='III.')
        elif kategori == 'penunjang':
            query = query.objects(butir__startswith='IV.')
        else:
            query = Pagination(self.request.GET, query.objects).paginate()

        return query

    def get(self, request, *args, **kwargs):
        obj = self.get_queryset()

        return HttpResponse(obj)

    def post(self, request, *args, **kwargs):
        butir = models.Butir(
            nama=request.POST.get('nama'),
            butir=request.POST.get('butir'),
            hasil=request.POST.get('hasil'),
            angka=request.POST.get('angka'),
            pelaksana=request.POST.get('pelaksana'),
            jenis=request.POST.get('jenis')
        )

        return create_exception(butir)


class ButirModifikasi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminOrLimitedAuthenticated,)

    def get_object(self):
        try:
            return models.Butir.objects.get(butir=self.kwargs['butir'])

        except models.Butir.DoesNotExist:
            raise exceptions.NotFound()

        except models.Butir.MultipleObjectsReturned:
            raise exceptions.NotAcceptable()

    def get(self, request, *args, **kwargs):
        return check_instance(self.get_object(),
                              models.Butir)

    def put(self, request, *args, **kwargs):
        def execute():
            try:
                return self.get_object().update(
                    set__nama=request.POST.get('nama'),
                    set__butir=request.POST.get('butir'),
                    set__hasil=request.POST.get('hasil'),
                    set__angka=request.POST.get('angka'),
                    set__pelaksana=request.POST.get('pelaksana'),
                    set__jenis=request.POST.get('jenis')
                )

            except errors.ValidationError as err:
                return json.dumps({
                    'detail': err.message
                })

        return check_instance(self.get_object(),
                              models.Butir,
                              execute())

    def destroy(self, request, *args, **kwargs):
        def execute():
            return self.get_object().delete()

        return check_instance(self.get_object(),
                              models.Butir,
                              execute())
