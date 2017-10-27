from django.http import HttpResponse
from rest_framework import generics
from . import models
import json
from .paginations import Pagination
from mongoengine import (ValidationError, NotUniqueError,
                         DoesNotExist, MultipleObjectsReturned)
# from django.contrib.auth import hashers


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

        try:
            butir.save()

            return HttpResponse(butir.to_json())

        except ValidationError as err:
            return HttpResponse(json.dumps(err.to_dict()))

        except NotUniqueError:
            return HttpResponse(json.dumps({
                'detail': 'Tried to save duplicate unique keys'
            }))


class ButirModifikasi(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        try:
            q = models.Butir.objects.get(butir=self.kwargs['butir'])
            return q

        except DoesNotExist:
            return HttpResponse(json.dumps({
                'detail': 'Matching query does not exist.'
            }))

        except MultipleObjectsReturned:
            return HttpResponse(json.dumps({
                'detail': 'Multiple object found'
            }))

    def get(self, request, *args, **kwargs):
        butir = self.get_object()

        if isinstance(butir, models.Butir):
            return HttpResponse(butir.to_json())
        else:
            return butir

    def put(self, request, *args, **kwargs):
        butir = self.get_object()

        if isinstance(butir, models.Butir):
            butir.update(
                set__nama=request.POST.get('nama'),
                set__butir=request.POST.get('butir'),
                set__hasil=request.POST.get('hasil'),
                set__angka=request.POST.get('angka'),
                set__pelaksana=request.POST.get('pelaksana'),
                set__jenis=request.POST.get('jenis')
            )

            butir.reload()

            return HttpResponse(butir.to_json())

        else:
            return butir

    def destroy(self, request, *args, **kwargs):
        butir = self.get_object()

        if isinstance(butir, models.Butir):
            butir.delete()
            return HttpResponse(butir.to_json())
        else:
            return butir
