from django.http import HttpResponse
from rest_framework import generics
from . import models


# Create your views here.
class Butir(generics.ListCreateAPIView):
    def get_queryset(self):
        q = models.Butir.objects.to_json()

        return q

    def get(self, request, *args, **kwargs):
        obj = self.get_queryset()
        return HttpResponse(obj)

    def post(self, request, *args, **kwargs):
        pass
