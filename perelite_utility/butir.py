import json
from django.http import HttpResponse
from rest_framework import generics
from . import models
from .helpers import (create_exception, check_instance)
from .paginations import Pagination


# Create your views here.
class Butir(generics.ListCreateAPIView):
    def get_queryset(self):
        q = Pagination(self.request.GET, models.Butir.objects)

        return q.paginate()

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
    def get_object(self):
        try:
            return models.Butir.objects.get(butir=self.kwargs['butir'])

        except models.Butir.DoesNotExist:
            return json.dumps({
                'detail': 'Matching query does not exist.'
            })

        except models.Butir.MultipleObjectsReturned:
            return json.dumps({
                'detail': 'Document not unique.'
            })

    def get(self, request, *args, **kwargs):
        return check_instance(self.get_object(),
                              models.Butir)

    def put(self, request, *args, **kwargs):
        def execute():
            return self.get_object().update(
                set__nama=request.POST.get('nama'),
                set__butir=request.POST.get('butir'),
                set__hasil=request.POST.get('hasil'),
                set__angka=request.POST.get('angka'),
                set__pelaksana=request.POST.get('pelaksana'),
                set__jenis=request.POST.get('jenis')
            )

        return check_instance(self.get_object(),
                              models.Butir,
                              execute())

    def destroy(self, request, *args, **kwargs):
        def execute():
            return self.get_object().delete()

        return check_instance(self.get_object(),
                              models.Butir,
                              execute())
