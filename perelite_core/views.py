import json
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import exceptions
from . import models
from .proses import paket
from perelite_utility import permissions, paginations
from perelite_utility.helpers import (create_exception,
                                      check_instance)


class Tugas(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        tugas = paginations.Pagination(self.request.GET, models.Tugas.objects)

        return tugas.paginate()

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.get_queryset())

    def post(self, request, *args, **kwargs):
        pkt = json.loads(request.POST.get('paket_tugas'))

        tugas = models.Tugas(
            tanggal=request.POST.get('tanggal'),
            kategori=request.POST.get('kategori'),
            butir=request.POST.get('butir'),
            angka=request.POST.get('angka'),
            satuan=request.POST.get('satuan'),
            uraian_singkat=request.POST.get('uraian_singkat'),
            paket_tugas=paket(pkt),
        )

        return create_exception(tugas)
