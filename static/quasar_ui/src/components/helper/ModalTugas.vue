<template>
    <q-modal v-model="modalStats" maximized
             :content-classes="['layout-padding', 'pt-3']">
        <h4>Form Tugas</h4>

        <div class="row md-gutter">
            <div class="col-md-4">
                <q-field
                    helper="Pilih tanggal kegiatan"
                    :error="$v.form.tanggal.$error"
                    error-label="Harus diisi">
                    <q-datetime
                        color="secondary"
                        float-label="Tanggal awal"
                        v-model="form.tanggal"
                        type="date"
                        @blur="$v.form.tanggal.$touch()"
                    ></q-datetime>
                </q-field>
            </div>
            <div class="col-md-4">
                <q-field
                    helper=""
                    :error="$v.form.jenis.$error"
                    error-label="Harus diisi">
                    <q-select
                        color="secondary"
                        float-label="Kategori Tugas"
                        v-model="form.jenis"
                        :options="opsiJenis"
                        @blur="$v.form.jenis.$touch()"
                    ></q-select>
                </q-field>
            </div>
            <div class="col-md-4">
                <q-field
                    helper=""
                    :error="$v.form.butir.$error"
                    error-label="Harus diisi">
                    <q-select
                        color="secondary"
                        float-label="Butir Tugas"
                        v-model="form.butir"
                        :options="opsiJenis"
                        :filter="true"
                        @blur="$v.form.butir.$touch()"
                    ></q-select>
                </q-field>
            </div>
        </div>

        <div class="row md-gutter">
            <div class="col-md-6">
                <q-field
                    helper="Angka perolehan tugas"
                    :error="$v.form.angka.$error"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Angka"
                        v-model="form.angka"
                        type="number"
                        readonly disable :before="[
                            {icon: 'filter 9 plus', content: true}
                        ]"
                        @blur="$v.form.angka.$touch()"
                    ></q-input>
                </q-field>
            </div>
            <div class="col-md-6">
                <q-field
                    helper="Satuan: LK, LB, TN, Lainnya"
                    :error="$v.form.satuan.$error"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Satuan Hasil"
                        v-model="form.satuan"
                        type="text"
                        readonly disable :before="[
                            {icon: 'insert drive file', content: true}
                        ]"
                        @blur="$v.form.satuan.$touch()"
                    ></q-input>
                </q-field>
            </div>
        </div>

        <div class="row md-gutter">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.form.uraian_singkat.$error"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Uraian Singkat"
                        v-model="form.uraian_singkat"
                        type="textarea"
                        @blur="$v.form.uraian_singkat.$touch()"
                    ></q-input>
                </q-field>
            </div>
        </div>

        <div class="row mt-4 mb-4">
            <div class="col">
                <app-tabs-tugas></app-tabs-tugas>
            </div>
        </div>

        <div class="row mt-3 mb-4">
            <div class="col">
                <q-btn color="primary"
                       @click="onFormTugasSubmit"
                       icon="save">
                    Simpan
                </q-btn>
                <q-btn color="grey-5"
                       @click="onModalClose"
                       icon="not interested">
                    Batal
                </q-btn>
            </div>
        </div>
    </q-modal>
</template>

<script>
    import {required} from 'vuelidate/lib/validators';
    import {
        QBtn,
        QModal,
        QField,
        QInput,
        QDatetime,
        QSelect
    } from 'quasar';

    import appTabsTugas from './TabsTugas.vue';

    export default {
        data() {
            return {
                form: {
                    tanggal: null,
                    jenis: null,
                    butir: null,
                    angka: 0.,
                    satuan: null,
                    uraian_singkat: null,
                    uraian_lengkap: null
                },
                opsiJenis: [
                    {label: 'Pendidikan', value: 'pendidikan'},
                    {label: 'Kerekayasaan', value: 'kerekayasaan'},
                    {label: 'Profesi', value: 'profesi'},
                    {label: 'Penunjang', value: 'penunjang'},
                ]
            }
        },
        validations: {
            form: {
                tanggal: {required},
                jenis: {required},
                butir: {required},
                angka: {required},
                satuan: {required},
                uraian_singkat: {required},
                uraian_lengkap: {required}
            }
        },
        components: {
            QBtn,
            QModal,
            QField,
            QInput,
            QDatetime,
            QSelect,
            appTabsTugas
        },
        methods: {
            onModalClose() {
                this.$v.form.$reset();
                this.$store.commit('setShowModalTugas', false);
            },
            onFormTugasSubmit() {
                console.log('submit');
            }
        },
        computed: {
            modalStats() {
                return this.$store.getters.getShowModalTugas;
            }
        }
    }
</script>

<style>
</style>
