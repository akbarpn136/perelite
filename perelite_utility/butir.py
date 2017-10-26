from django.http import HttpResponse
from rest_framework import generics
from . import models
import json
from .paginations import Pagination
from mongoengine import ValidationError, NotUniqueError


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

        except NotUniqueError as nu:
            return HttpResponse(json.dumps({
                'butir': 'Tried to save duplicate unique keys'
            }))
