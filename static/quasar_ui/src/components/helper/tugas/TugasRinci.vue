<template>
    <q-card class="bg-white no-margin">
        <q-card-title>
            <q-btn color="primary" class="print-hide" small outline @click="onCetak()">
                <q-icon name="print"></q-icon>
            </q-btn>
            <q-btn color="green" class="print-hide" small outline
                   @click="$router.push({name: 'ubahTugas', params: {pk: tugas.pk}})">
                <q-icon name="edit"></q-icon>
            </q-btn>
            <q-btn color="negative" class="print-hide" small outline @click="onDeleteTugas()">
                <q-icon name="delete"></q-icon>
            </q-btn>
            <q-btn color="gray"
                   flat
                   slot="right"
                   class="print-hide"
                   @click="$router.go(-1)">
                <q-icon name="clear"></q-icon>
            </q-btn>
        </q-card-title>
        <q-card-separator></q-card-separator>
        <q-card-main>
            <div id="tgs" v-if="tugas._cls === 'Lk'" ref="tgs">
                <table class="q-table cell-separator compact full-width">
                    <tbody>
                    <tr>
                        <td class="text-center" rowspan="4">
                            <img src="../../../assets/logo_bppt.jpg" alt="logo" width="92">
                        </td>
                        <td class="text-center">
                            <h4>{{tugas.nama}}</h4>
                        </td>
                        <td class="text-center" colspan="2">
                            <b>{{tugas.kode_peran}}</b>
                        </td>
                    </tr>
                    <tr>
                        <td class="text-center" rowspan="2">
                            <dl>
                                <dt style="font-weight: normal;">Program</dt>
                                <dd class="uppercase">
                                    <h6 class="no-margin">{{tugas.program}}</h6>
                                </dd>
                            </dl>
                        </td>
                        <td class="text-right">No.</td>
                        <td class="text-right">
                            {{tugas.nomor}}
                        </td>
                    </tr>
                    <tr>
                        <td class="text-right">Ref.</td>
                        <td class="text-right">{{tugas.referensi}}</td>
                    </tr>
                    <tr>
                        <td class="text-center">
                            <dl>
                                <dt style="font-weight: normal;">WBS/WP</dt>
                                <dd class="uppercase">
                                    <h6 class="no-margin">{{tugas.wbs_wp}}</h6>
                                </dd>
                            </dl>
                        </td>
                        <td class="text-right" colspan="2">{{tugas.tanggal.$date | tgl}}</td>
                    </tr>
                    <tr>
                        <td class="text-left" colspan="4">
                            Butir kegiatan: {{tugas.butir}}
                        </td>
                    </tr>
                    </tbody>
                </table>
                <div v-html="tugas.uraian_lengkap" class="mt-4"></div>
                <table class="q-table cell-separator bordered compact full-width" style="margin-bottom: 0">
                    <tbody>
                    <tr>
                        <td class="text-left" colspan="2">
                            Dari:
                        </td>
                        <td class="text-left" colspan="2">
                            Kepada:
                        </td>
                    </tr>
                    <tr>
                        <td>Nama</td>
                        <td>{{tugas.nama_pemberi}}</td>
                        <td>Nama</td>
                        <td>{{user}}</td>
                    </tr>
                    <tr>
                        <td>Peran</td>
                        <td>{{tugas.peran_pemberi}}</td>
                        <td>Peran</td>
                        <td>{{tugas.kode_peran}}</td>
                    </tr>
                    <tr>
                        <td class="vertical-top">Ttd</td>
                        <td><br><br><br><br></td>
                        <td class="vertical-top">Ttd</td>
                        <td><br><br><br><br></td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <div id="tgs" v-if="checkTugas(tugas)" ref="tgs">
                <div class="row md-gutter">
                    <div class="col-2 self-center">
                        <img
                            src="../../../assets/logbook.png"
                            alt="logbook"
                            v-if="tugas._cls === 'Lb'">
                        <img
                            src="../../../assets/technicalNote.png"
                            alt="logbook"
                            v-if="tugas._cls === 'Tn'">
                    </div>
                    <div class="col-10">
                        <div class="row justify-between" style="margin-bottom: 105px;">
                            <div class="col-6"></div>
                            <div class="col-6">
                                <table class="q-table cell-separator compact full-width">
                                    <tr>
                                        <td>Tanggal</td>
                                        <td>{{tugas.tanggal.$date | tgl}}</td>
                                    </tr>
                                </table>
                            </div>
                        </div>
                        <div class="row justify-between" style="margin-bottom: 65px;">
                            <div class="col-4"></div>
                            <div class="col-7 text-right">
                                <img src="../../../assets/logo_bppt.jpg" alt="logo" width="92">
                            </div>
                        </div>
                        <div class="row justify-between" style="margin-bottom: 25px;">
                            <div class="col-4"></div>
                            <div class="col-7 text-right">
                                <h5>{{tugas.nomor}}</h5>
                                <h5>{{tugas.kode_peran}}</h5>
                            </div>
                        </div>
                        <div class="row" style="margin-bottom: 25px;">
                            <div class="col text-right">
                                <h2>{{tugas.judul}}</h2>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col text-center">
                                <h6 class="uppercase">{{tugas.unit_kerja}}</h6>
                                <h6 class="uppercase">{{tugas.pusat_kerja}}</h6>
                            </div>
                        </div>
                    </div>
                </div>
                <table class="q-table cell-separator bordered compact full-width" style="margin-top: 25px;">
                    <tbody>
                    <tr>
                        <td class="text-left" colspan="2">
                            Dibuat oleh:
                        </td>
                        <td class="text-left" colspan="2">
                            Diperiksa oleh:
                        </td>
                        <td class="text-left" colspan="2">
                            Disetujui oleh:
                        </td>
                    </tr>
                    <tr>
                        <td>Nama</td>
                        <td>{{user}}</td>
                        <td>Nama</td>
                        <td>{{tugas.nama_pemeriksa}}</td>
                        <td>Nama</td>
                        <td>{{tugas.nama_penyetuju}}</td>
                    </tr>
                    <tr>
                        <td>Peran</td>
                        <td>{{tugas.kode_peran}}</td>
                        <td>Peran</td>
                        <td>{{tugas.peran_pemeriksa}}</td>
                        <td>Peran</td>
                        <td>{{tugas.peran_penyetuju}}</td>
                    </tr>
                    <tr>
                        <td class="vertical-top">Ttd</td>
                        <td><br><br><br><br></td>
                        <td class="vertical-top">Ttd</td>
                        <td><br><br><br><br></td>
                        <td class="vertical-top">Ttd</td>
                        <td><br><br><br><br></td>
                    </tr>
                    </tbody>
                </table>
                <div v-html="tugas.uraian_lengkap" class="mt-4"></div>
            </div>
        </q-card-main>
    </q-card>
</template>

<script>
    import {
        Dialog,
        Toast,
        QBtn,
        QIcon,
        QCard,
        QCardTitle,
        QCardSeparator,
        QCardMain,
    } from 'quasar';

    import html2pdf from 'html2pdf.js/src';
    import {HapusTugas} from '../../../http/tugas';
    import * as _ from 'lodash';

    export default {
        name: "tugas-rinci",
        components: {
            QBtn,
            QIcon,
            QCard,
            QCardTitle,
            QCardSeparator,
            QCardMain,
        },
        props: ['trigger'],
        created() {
            this.tugas = this.$store.getters.getTugasRinci;
            this.user = JSON.parse(localStorage.getItem('qwerty')).user;
        },
        data() {
            return {
                tugas: null,
                user: null
            }
        },
        methods: {
            checkTugas(tugas) {
                return (tugas._cls === 'Lb') || (tugas._cls === 'Tn')
            },
            onCetak() {
                html2pdf(this.$refs.tgs, {
                    margin: 1,
                    enableLinks: true,
                    filename: `${this.$refs.tgs.id}.pdf`,
                    image: {type: 'jpeg', quality: 0.98},
                    html2canvas: {dpi: 300, letterRendering: true},
                    jsPDF: {unit: 'cm', format: 'a4', orientation: 'portrait'}
                });
            },
            onDeleteTugas() {
                let selected_tugas = this.$store.getters.getTugasRinci;
                Dialog.create({
                    title: 'Anda yakin?',
                    message: 'Tugas yang dihapus tidak dapat dikembalikan lagi.',
                    buttons: [
                        {
                            label: 'Batal'
                        },
                        {
                            label: 'Hapus',
                            color: 'negative',
                            handler: () => {
                                HapusTugas(selected_tugas.pk).then(() => {
                                    Toast.create.positive('Tugas berhasil dihapus');
                                    this.$emit('trigger', true);
                                    this.$router.go(-1);
                                }).catch((err) => {
                                    _.forEach(err.response.data, (v, k) => {
                                        Toast.create.negative(`${k}: ${v}`);
                                    });
                                });
                            }
                        }
                    ]
                });
            }
        },
        filters: {
            tgl: function (value) {
                let options = {year: 'numeric', month: 'long', day: 'numeric'};
                return new Date(value).toLocaleDateString('id', options);
            }
        }
    }
</script>

<style>
</style>
