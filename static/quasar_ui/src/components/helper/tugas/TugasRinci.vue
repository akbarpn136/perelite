<template>
    <div class="layout-padding">
        <div v-if="this.tugas._cls === 'Lk'">
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
                    <td class="text-right" colspan="2">{{tugas.tanggal | tgl}}</td>
                </tr>
                <tr>
                    <td class="text-left" colspan="4">
                        Butir kegiatan: {{tugas.butir}}
                    </td>
                </tr>
                </tbody>
            </table>
            <div v-html="tugas.uraian_lengkap" class="mt-4"></div>
            <table class="q-table cell-separator compact full-width" style="margin-bottom: 0">
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
    </div>
</template>

<script>
    import {
        QBtn,
    } from 'quasar';

    export default {
        name: "tugas-rinci",
        components: {
            QBtn,
        },
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
