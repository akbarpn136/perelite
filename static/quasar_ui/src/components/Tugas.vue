<template>
    <div>
        <q-card class="bg-white no-margin">
            <q-card-title>
                Daftar {{$route.name | capitalize | splitString}}
            </q-card-title>
            <q-card-separator></q-card-separator>
            <q-card-main>
                <div class="row mb-4 md-gutter">
                    <div class="col">
                        <q-field
                            helper="Pilih data mulai tanggal"
                            :error="$v.form.tglAwal.$error"
                            error-label="Harus diisi">
                            <q-datetime
                                color="secondary"
                                float-label="Tanggal awal"
                                v-model="form.tglAwal"
                                type="date"
                                @change="onDateChange"
                            ></q-datetime>
                        </q-field>
                    </div>

                    <div class="col">
                        <q-field
                            helper="Pilih data sampai tanggal"
                            :error="$v.form.tglAkhir.$error"
                            error-label="Harus diisi">
                            <q-datetime
                                color="secondary"
                                float-label="Tanggal akhir"
                                v-model="form.tglAkhir"
                                type="date"
                                @change="onDateChange"
                            ></q-datetime>
                        </q-field>
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
                    <tr v-for="(n,i) in 10" :key="i">
                        <td data-th="Tanggal" class="text-left">Item #1</td>
                        <td data-th="Uraian kegiatan" class="text-right">$10.11</td>
                        <td data-th="Butir" class="text-right">101</td>
                        <td data-th="Satuan" class="text-right">101</td>
                        <td data-th="Bukti" class="text-right">101</td>
                    </tr>
                    </tbody>
                </table>

                <div class="row justify-start">
                    <div class="col-4">
                        <q-pagination v-model="page"
                                      :max="17"
                                      class="float-left"
                                      color="secondary"></q-pagination>
                    </div>
                </div>
            </q-card-main>
        </q-card>
    </div>
</template>

<script>
    import {required} from 'vuelidate/lib/validators';
    import {
        QBtn,
        QIcon,
        QCard,
        QCardTitle,
        QCardMain,
        QCardSeparator,
        QPagination,
        QField,
        QInput,
        QDatetime
    } from 'quasar';

    export default {
        data() {
            return {
                page: 1,
                form: {
                    tglAwal: '',
                    tglAkhir: ''
                }
            }
        },
        validations: {
            form: {
                tglAwal: {required},
                tglAkhir: {required},
            }
        },
        created() {
        },
        methods: {
            onDateChange() {
                if (!this.$v.form.tglAwal.$invalid &&
                    !this.$v.form.tglAkhir.$invalid) {
                    console.log('alhamdulillah');
                } else {
                    this.$v.form.$touch();
                }
            }
        },
        components: {
            QBtn,
            QIcon,
            QCard,
            QCardTitle,
            QCardMain,
            QCardSeparator,
            QPagination,
            QField,
            QInput,
            QDatetime
        },
        filters: {
            capitalize: function (value) {
                if (!value) return '';
                value = value.toString();
                return value.charAt(0).toUpperCase() + value.slice(1);
            },
            splitString: function (value) {
                return value.replace(/([A-Z]+)/g, " $1").replace(/([A-Z][a-z])/g, " $1");
            }
        }
    }
</script>

<style>
</style>
