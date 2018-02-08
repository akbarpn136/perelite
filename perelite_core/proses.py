import uuid
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
                kode_tugas=uuid.uuid4().hex,
            )

            paket_tugas.append(lk)

        elif p.get('nama') == 'LOGBOOK':
            lb = models.Lb(
                nama=p['nama'],
                nomor=p['nomor'],
                kode_peran=p['kode_peran'],
                judul=p['judul'],
                unit_kerja=p['unit_kerja'],
                pusat_kerja=p['pusat_kerja'],
                uraian_lengkap=p['uraian_lengkap'],
                nama_pemeriksa=p['nama_pemeriksa'],
                peran_pemeriksa=p['peran_pemeriksa'],
                nama_penyetuju=p['nama_penyetuju'],
                peran_penyetuju=p['peran_penyetuju'],
            )

            paket_tugas.append(lb)
        elif p.get('nama') == 'TECHNICAL NOTE':
            tn = models.Tn(
                nama=p['nama'],
                nomor=p['nomor'],
                kode_peran=p['kode_peran'],
                judul=p['judul'],
                unit_kerja=p['unit_kerja'],
                pusat_kerja=p['pusat_kerja'],
                uraian_lengkap=p['uraian_lengkap'],
                nama_pemeriksa=p['nama_pemeriksa'],
                peran_pemeriksa=p['peran_pemeriksa'],
                nama_penyetuju=p['nama_penyetuju'],
                peran_penyetuju=p['peran_penyetuju'],
            )

            paket_tugas.append(tn)
        elif p.get('nama') == 'OTHERS':
            pass

    return paket_tugas
