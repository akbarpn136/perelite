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

                <q-infinite-scroll :handler="refresher"
                                   ref="infiniteScroll">
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
                        <tr v-for="(tugas, idx) in daftarTugas" :key="tugas._id.$oid">
                            <td data-th="Uraian kegiatan" class="text-left">#{{idx+1}} {{tugas.uraian_singkat}}</td>
                            <td data-th="Tanggal" class="text-right">{{tugas.tanggal.$date | tgl}}</td>
                            <td data-th="Butir" class="text-right">{{tugas.butir}}</td>
                            <td data-th="Satuan" class="text-right">{{tugas.satuan}}</td>
                            <td data-th="Bukti" class="text-right">
                                <p v-for="pkt in tugas.paket_tugas">
                                    <a @click.prevent="onPaketTugasClick(pkt.kode_tugas)">{{pkt._cls}} {{pkt.nomor}}</a>
                                </p>
                            </td>
                        </tr>
                        <tr v-if="noData">
                            <td colspan="5" class="text-center">
                                <q-chip color="info" square>Tidak ada data</q-chip>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    <div slot="message" class="row justify-center">
                        <q-spinner-dots :size="35"></q-spinner-dots>
                    </div>
                </q-infinite-scroll>
            </q-card-main>
        </q-card>
    </div>
</template>

<script>
    import {
        debounce,
        QChip,
        QCard,
        QCardTitle,
        QCardMain,
        QCardSeparator,
        QField,
        QDatetimeRange,
        Toast,
        QInfiniteScroll,
        QSpinnerDots
    } from 'quasar';

    import {LihatTugas} from '../http/tugas';
    import * as _ from 'lodash';

    export default {
        components: {
            QChip,
            QCard,
            QCardTitle,
            QCardMain,
            QCardSeparator,
            QField,
            QDatetimeRange,
            Toast,
            QInfiniteScroll,
            QSpinnerDots
        },
        data() {
            return {
                page: 1,
                datetimeRange: {
                    from: null,
                    to: null
                },
                kategori: null,
                daftarTugas: [],
                totalAngka: 0,
                totalTugas: 0,
                tglAwal: null,
                tglAkhir: null,
                noData: false,
            }
        },
        created() {
            this.kategori = this.$route.name;
        },
        methods: {
            onDateChange() {
                if (this.datetimeRange.from && this.datetimeRange.to) {
                    this.tglAwal = new Date(this.datetimeRange.from).toLocaleDateString('id');
                    this.tglAkhir = new Date(this.datetimeRange.to).toLocaleDateString('id');

                    this.daftarTugas = [];
                    this.$refs.infiniteScroll.reset();
                    this.$refs.infiniteScroll.resume();
                }
            },
            onPaketTugasClick(kode_tugas) {
                console.log(kode_tugas);
            },
            refresher(index, done) {
                setTimeout(() => {
                    LihatTugas(this.kategori, this.tglAwal, this.tglAkhir, index).then(res => {
                        let results = JSON.parse(res.data.results);
                        this.totalAngka = JSON.parse(res.data['total_angka']);
                        this.totalTugas = JSON.parse(res.data['total_tugas']);
                        this.daftarTugas = this.daftarTugas.concat(results);
                        console.log(this.daftarTugas.length);

                        this.noData = (this.totalTugas === 0) ? true : false;

                        if (this.daftarTugas.length >= this.totalTugas) {
                            this.$refs.infiniteScroll.stop();
                        }
                        done();
                    }).catch(err => {
                        _.forEach(err.response.data, (v, k) => {
                            Toast.create.negative(`${k}: ${v}`);
                        });
                        done();
                    });
                }, 1000);
            }
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
            tgl: function (value) {
                let options = {year: 'numeric', month: 'long', day: 'numeric'};
                return new Date(value).toLocaleDateString('id', options);
            }
        }
    }
</script>

<style>
</style>
