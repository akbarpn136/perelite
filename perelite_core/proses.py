import json
from . import models


def paket(package):
    paket_tugas = []
    for p in package:
        p = json.loads(p)

        if p.get('nama') == 'LEMBAR KERJA':
            lk = models.Lk(
                nama=p['nama'],
                kode_peran=p['kode_peran'],
                nomor=p['nomor'],
                referensi=p['referensi'],
                program=p['program'],
                wbs_wp=p['wbs_wp'],
                uraian_lengkap=p['uraian_lengkap'],
                nama_pemberi=p['nama_pemberi'],
                peran_pemberi=p['peran_pemberi'],
            )

            paket_tugas.append(lk)

        elif p.get('nama') == 'LOGBOOK':
            pass
        elif p.get('nama') == 'TECHNICAL NOTE':
            pass
        elif p.get('nama') == 'OTHERS':
            pass

    return paket_tugas
