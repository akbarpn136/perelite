from mongoengine import *
from perelite_utility.models import Personil

OPSI_PELAKSANA = (
    'pendidikan',
    'kerekayasaan',
    'profesi',
    'penunjang',
)


class Lk(EmbeddedDocument):
    nama = StringField(default='LEMBAR KERJA')
    kode_tugas = StringField(required=True)
    kode_peran = StringField(required=True)
    nomor = StringField(required=True)
    referensi = StringField(required=True)
    program = StringField(required=True)
    wbs_wp = StringField(required=True)
    uraian_lengkap = StringField(required=True)
    nama_pemberi = StringField(required=True)
    peran_pemberi = StringField(required=True)


class Lb(EmbeddedDocument):
    nama = StringField(default='LEMBAR KERJA')
    nomor = StringField(required=True)
    kode_peran = StringField(required=True)
    judul = StringField(required=True)
    unit_kerja = StringField(required=True)
    pusat_kerja = StringField(required=True)
    uraian_lengkap = StringField(required=True)
    nama_pemeriksa = StringField(required=True)
    peran_pemeriksa = StringField(required=True)
    nama_penyetuju = StringField(required=True)
    peran_penyetuju = StringField(required=True)


class Tugas(Document):
    tanggal = DateTimeField(required=True)
    owner = ReferenceField(Personil, reverse_delete_rule=CASCADE)
    kategori = StringField(required=True, choices=OPSI_PELAKSANA)
    butir = StringField(required=True)
    angka = DecimalField(required=True, min_value=0)
    satuan = StringField(required=True)
    uraian_singkat = StringField(required=True)
    paket_tugas = ListField(GenericEmbeddedDocumentField())
