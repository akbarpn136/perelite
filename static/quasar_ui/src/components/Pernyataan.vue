<template>
    <!-- if you want automatic padding use "layout-padding" class -->
    <div class="bg-white">
        <!-- your content -->
        <q-card class="no-margin">
            <q-card-title>Surat Pernyataan</q-card-title>
            <q-card-main>
                <q-field class="full-width"
                         helper="Jenis tugas"
                         :error="$v.form.jenis.$error"
                         error-label="Tidak boleh kosong">
                    <q-select
                        stack-label="Kategori"
                        color="secondary"
                        separator
                        v-model="form.jenis"
                        :options="options"
                        @blur="$v.form.jenis.$touch()"></q-select>
                </q-field>

                <q-field class="full-width"
                         helper=""
                         :error="$v.form.tglAwal.$error"
                         error-label="Tidak boleh kosong">
                    <q-datetime stack-label="Tanggal Awal"
                                v-model="form.tglAwal"
                                color="secondary"
                                type="date"
                                @blur="$v.form.tglAwal.$touch()"></q-datetime>
                </q-field>

                <q-field class="full-width"
                         helper=""
                         :error="$v.form.tglAkhir.$error"
                         error-label="Tidak boleh kosong">
                    <q-datetime stack-label="Tanggal Akhir"
                                v-model="form.tglAkhir"
                                color="secondary"
                                type="date"
                                @blur="$v.form.tglAkhir.$touch()"></q-datetime>
                </q-field>

                <q-btn loader
                       color="primary mt-2"
                       class="full-width"
                       @click="onButtonProsesClick">
                    PROSES
                    <span slot="loading">
                        <q-spinner-puff class="on-left"></q-spinner-puff>
                        PROSES
                    </span>
                </q-btn>
            </q-card-main>
        </q-card>
    </div>
</template>

<script>
    import {required} from 'vuelidate/lib/validators';
    import {
        QBtn,
        QInput,
        QSelect,
        QField,
        QSideLink,
        QDatetime,
        QSpinnerPuff,
        QCard,
        QCardTitle,
        QCardMain,
        QCardSeparator,
        Toast
    } from 'quasar';

    export default {
        data() {
            return {
                form: {
                    jenis: '',
                    tglAwal: '',
                    tglAkhir: ''
                },
                options: [
                    {label: 'Pendidikan', value: 'Pendidikan'},
                    {label: 'Kerekayasaan', value: 'Kerekayasaan'},
                    {label: 'Profesi', value: 'Profesi'},
                    {label: 'Penunjang', value: 'Penunjang'},
                ]
            }
        },
        components: {
            QBtn,
            QInput,
            QSelect,
            QField,
            QSideLink,
            QDatetime,
            QSpinnerPuff,
            QCard,
            QCardTitle,
            QCardMain,
            QCardSeparator
        },
        validations: {
            form: {
                jenis: {required},
                tglAwal: {required},
                tglAkhir: {required},
            }
        },
        methods: {
            onButtonProsesClick(event, done) {
                const obj = {
                    'jenis': this.form.jenis,
                    'tglAwal': this.form.tglAwal,
                    'tglAkhir': this.form.tglAkhir,
                };

                this.$v.form.$touch();

                if (!this.$v.form.$error) {
                    setTimeout(() => {
                        console.log(obj);
                        done();
                    }, 2000)
                } else {
                    Toast.create.negative('Silahkan periksa lagi.');
                    done();
                }
            }
        }
    }
</script>

<style>
</style>
