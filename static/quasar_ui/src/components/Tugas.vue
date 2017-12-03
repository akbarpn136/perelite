<template>
    <div>
        <q-card class="bg-white no-margin">
            <q-card-title>
                Daftar {{$route.name | capitalize | splitString}}
            </q-card-title>
            <q-card-separator></q-card-separator>
            <q-card-main>
                <div class="row mb-4 md-gutter justify-between items-center">
                    <div class="col-md-6">
                        <q-field
                            icon="filter list"
                            label="Berdasarkan waktu">
                            <q-datetime-range
                                v-model="datetimeRange"
                                color="secondary"
                                class="full-width"
                                @change="onDateChange"
                            ></q-datetime-range>
                        </q-field>
                    </div>

                    <div class="col-md-3 text-right">
                        <q-chip icon="loyalty" color="secondary">
                            Total: {{totalAngka}}
                        </q-chip>
                    </div>
                </div>

                <table class="q-table bordered bg-white loose full-width horizontal-separator striped responsive">
                    <thead>
                    <tr>
                        <th class="text-left">Uraian kegiatan</th>
                        <th class="text-right">Tanggal</th>
                        <th class="text-right">Butir</th>
                        <th class="text-right">Satuan</th>
                        <th class="text-right">Bukti</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="tugas in daftarTugas" :key="tugas._id.$oid">
                        <td data-th="Uraian kegiatan" class="text-left">{{tugas.uraian_singkat}}</td>
                        <td data-th="Tanggal" class="text-right">{{tugas.tanggal.$date | tgl}}</td>
                        <td data-th="Butir" class="text-right">{{tugas.butir}}</td>
                        <td data-th="Satuan" class="text-right">{{tugas.satuan}}</td>
                        <td data-th="Bukti" class="text-right">
                            <p v-for="pkt in tugas.paket_tugas">
                                <a @click.prevent="onPaketTugasClick(pkt.kode_tugas)">{{pkt._cls}} {{pkt.nomor}}</a>
                            </p>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </q-card-main>
        </q-card>
    </div>
</template>

<script>
    import {
        QChip,
        QCard,
        QCardTitle,
        QCardMain,
        QCardSeparator,
        QField,
        QDatetimeRange,
        Toast
    } from 'quasar';

    import {LihatTugas} from '../http/tugas';
    import * as _ from 'lodash';

    export default {
        data() {
            return {
                page: 1,
                datetimeRange: {
                    from: null,
                    to: null
                },
                kategori: null,
                daftarTugas: [],
                totalAngka: 0
            }
        },
        created() {
            this.kategori = this.$route.name;
            this.onListTugas();
        },
        methods: {
            onDateChange() {
                if (this.datetimeRange.from && this.datetimeRange.to) {
                    let tglAwal = new Date(this.datetimeRange.from).toLocaleDateString('id');
                    let tglAkhir = new Date(this.datetimeRange.to).toLocaleDateString('id');

                    this.onListTugas(tglAwal, tglAkhir);
                }
            },
            onListTugas(tglAwal=null, tglAkhir=null) {
                LihatTugas(this.kategori, tglAwal, tglAkhir).then(res => {
                    let results = JSON.parse(res.data.results);
                    this.totalAngka = JSON.parse(res.data.count);
                    this.daftarTugas = results;
                }).catch(err => {
                    _.forEach(err.response.data, (v, k) => {
                        Toast.create.negative(`${k}: ${v}`);
                    })
                });
            },
            onPaketTugasClick(kode_tugas) {
                console.log(kode_tugas);
            }
        },
        components: {
            QChip,
            QCard,
            QCardTitle,
            QCardMain,
            QCardSeparator,
            QField,
            QDatetimeRange,
            Toast
        },
        filters: {
            capitalize: function (value) {
                if (!value) return '';
                value = value.toString();
                return value.charAt(0).toUpperCase() + value.slice(1);
            },
            splitString: function (value) {
                return value.replace(/([A-Z]+)/g, " $1").replace(/([A-Z][a-z])/g, " $1");
            },
            tgl: function(value) {
                let options = { year: 'numeric', month: 'long', day: 'numeric' };
                return new Date(value).toLocaleDateString('id', options);
            }
        }
    }
</script>

<style>
</style>
