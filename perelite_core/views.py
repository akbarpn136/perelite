import json
import datetime
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import exceptions
from . import models
from perelite_utility.models import Personil
from .proses import paket
from perelite_utility import permissions, paginations
from perelite_utility.helpers import (create_exception,
                                      check_instance)


class Tugas(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        tugasObj = {}
        user = Personil.objects.get(username=self.request.user.username)
        kategori = self.kwargs.get('kategori')
        tglAwal = self.request.GET.get('tglAwal')
        tglAkhir = self.request.GET.get('tglAkhir')

        if kategori == 'pendidikan':
            butir = 'I.'
        elif kategori == 'kerekayasaan':
            butir = 'II.'
        elif kategori == 'profesi':
            butir = 'III.'
        elif kategori == 'penunjang':
            butir = 'IV.'
        else:
            butir = ''

        obj = models.Tugas.objects

        if tglAwal and tglAkhir:
            obj = obj.filter(owner=user,
                             butir__startswith=butir,
                             tanggal__gte=datetime.datetime.strptime(tglAwal, '%d/%m/%Y'),
                             tanggal__lte=datetime.datetime.strptime(tglAkhir, '%d/%m/%Y'))

        else:
            obj = obj.filter(owner=user,
                             butir__startswith=butir)

        tugasObj['total_tugas'] = obj.count()
        tugas = paginations.Pagination(self.request.GET, obj.order_by('-tanggal')).paginate()
        tugasObj['total_angka'] = round(obj.sum('angka'), 3)
        tugasObj['results'] = tugas

        return json.dumps(tugasObj)

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.get_queryset())

    def post(self, request, *args, **kwargs):
        pkt = json.loads(request.POST.get('paket_tugas'))
        user = models.Personil.objects.get(username=request.user.username)

        tugas = models.Tugas(
            tanggal=request.POST.get('tanggal'),
            owner=user,
            kategori=request.POST.get('kategori'),
            butir=request.POST.get('butir'),
            angka=request.POST.get('angka'),
            satuan=request.POST.get('satuan'),
            uraian_singkat=request.POST.get('uraian_singkat'),
            paket_tugas=paket(pkt),
        )

        return create_exception(tugas)
