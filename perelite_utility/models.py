from mongoengine import *

OPSI_HASIL = (
    'Lembar Kerja',
    'Lembar Kerja/Logbook',
    'Lembar Kerja/Foto',
    'Benda Kerja/Lembar Kerja',
    'Logbook',
    'Surat Keputusan',
    'Technical Note',
)

OPSI_PELAKSANA = (
    'Perekayasa Pertama',
    'Perekayasa Pertama/Muda',
    'Perekayasa Muda',
    'Perekayasa Muda/Madya',
    'Perekayasa Madya',
    'Perekayasa Madya/Utama',
    'Perekayasa Utama',
    'Semua Jenjang',
)


# Create your models here.
class Butir(Document):
    nama = StringField(required=True)
    butir = StringField(max_length=120, required=True, unique=True)
    hasil = StringField(required=True, choices=OPSI_HASIL)
    angka = FloatField(required=True)
    pelaksana = StringField(required=True, choices=OPSI_PELAKSANA)
    jenis = StringField(required=True, choices=('Pendidikan', 'Kerekayasaan', 'Profesi', 'Penunjang'))

    meta = {
        'ordering': ['butir']
    }


class Profil(Document):
    nip = StringField(required=True)
    pendidikan = StringField()
    instansi = StringField()
    singkatan = StringField()
    pangkat = StringField(required=True)
    jabatan = StringField(required=True)


class Personil(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    token = StringField(required=True)
    nama_depan = StringField()
    nama_belakang = StringField()
    email = EmailField(required=True)
    profil = ReferenceField(Profil, reverse_delete_rule=CASCADE)
