import json
import datetime
from django.http import HttpResponse
from mongoengine import errors
from rest_framework import generics
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


class TugasModifikasi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsOwnerTugas,)
    tugas = ''

    def dispatch(self, request, *args, **kwargs):
        self.tugas = self.get_object()
        return super(TugasModifikasi, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        try:
            tgs = models.Tugas.objects.get(pk=self.kwargs.get('tugas_id'))

            return tgs
        except models.Tugas.DoesNotExist:
            self.tugas = False

        except errors.ValidationError:
            self.tugas = False

    def get(self, request, *args, **kwargs):
        return check_instance(self.get_object(),
                              models.Tugas)

    def put(self, request, *args, **kwargs):
        def execute():
            pkt = json.loads(request.POST.get('paket_tugas'))
            user = models.Personil.objects.get(username=request.user.username)

            try:
                return self.get_object().update(
                    set__tanggal=request.POST.get('nama'),
                    set__owner=user,
                    set__kategori=request.POST.get('hasil'),
                    set__butir=request.POST.get('angka'),
                    set__angka=request.POST.get('pelaksana'),
                    set__satuan=request.POST.get('jenis'),
                    set__uraian_singkat=request.POST.get('jenis'),
                    set__paket_tugas=paket(pkt),
                )

            except errors.ValidationError as err:
                return json.dumps({
                    'detail': err.message
                })

        return check_instance(self.get_object(),
                              models.Tugas,
                              execute())

    def destroy(self, request, *args, **kwargs):
        def execute():
            return self.get_object().delete()

        return check_instance(self.get_object(),
                              models.Tugas,
                              execute())
