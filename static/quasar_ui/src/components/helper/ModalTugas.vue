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
                        @change="onSelectKategoriChange"
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
                        :options="opsiButir"
                        :filter="true"
                        @blur="$v.form.butir.$touch()"
                        @change="onSelectButirChange"
                        :disable="!isButirActive"
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
    import * as _ from 'lodash';
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
    import {GetButir} from '../../http/butir';

    export default {
        data() {
            return {
                koleksiButir: null,
                form: {
                    tanggal: null,
                    jenis: null,
                    butir: null,
                    angka: 0.,
                    satuan: null,
                    uraian_singkat: null
                },
                opsiJenis: [
                    {label: 'Pendidikan', value: 'pendidikan'},
                    {label: 'Kerekayasaan', value: 'kerekayasaan'},
                    {label: 'Profesi', value: 'profesi'},
                    {label: 'Penunjang', value: 'penunjang'},
                ],
                opsiButir: [],
                isButirActive: false,
                dataActiveTabs: {
                    TabName: null,
                    LkActive: false,
                    LbActive: false,
                    TnActive: false,
                    OthersActive: false
                }
            }
        },
        validations: {
            form: {
                tanggal: {required},
                jenis: {required},
                butir: {required},
                angka: {required},
                satuan: {required},
                uraian_singkat: {required}
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
                this.clearForm();
            },
            onSelectKategoriChange() {
                if (!this.isButirActive) {
                    this.isButirActive = true;
                }
                this.opsiButir = [];
                this.onGetButir(this.form.jenis);
            },
            onSelectButirChange() {
                const selectedButir = _.filter(this.koleksiButir, (el) => {
                    return (el.butir === this.form.butir);
                });

                this.form.angka = selectedButir[0].angka;
                this.form.satuan = selectedButir[0].hasil;
                this.checkActiveTabs(this.form.satuan);
            },
            onFormTugasSubmit() {
                console.log('submit');
            },
            onGetButir(params = null) {
                return GetButir(params).then((res) => {
                    this.koleksiButir = res.data;
                    _.forEach(res.data, (btr) => {
                        this.opsiButir.push({
                            label: btr.nama,
                            value: btr.butir,
                            stamp: btr.angka.toString()
                        });
                    });
                }).catch((err) => {
                    console.log(err.response);
                });
            },
            checkActiveTabs(cond) {
                switch (cond) {
                    case 'Lembar Kerja':
                        this.setTabs('lk', true, false, false, false);

                        break;
                    case 'Lembar Kerja/Logbook':
                        this.setTabs('lk', true, true, false, false);

                        break;
                    case 'Lembar Kerja/Foto':
                        this.setTabs('lk', true, false, false, false);

                        break;
                    case 'Benda Kerja/Lembar Kerja':
                        this.setTabs('lk', true, false, false, false);

                        break;
                    case 'Logbook':
                        this.setTabs('lb', false, true, false, false);

                        break;
                    case 'Technical Note':
                        this.setTabs('tn', false, false, true, false);

                        break;
                    default:
                        this.setTabs('ot', false, false, false, true);
                }
                this.$store.commit('setActiveTaskTab', this.dataActiveTabs);
            },
            setTabs(TabName=null,
                    LkActive=false,
                    LbActive=false,
                    TnActive=false,
                    OthersActive=false) {
                let opsi = {TabName, LkActive, LbActive, TnActive, OthersActive};

                _.forEach(opsi, (v, k) => {
                    this.dataActiveTabs[k] = v;
                });
            },
            clearForm() {
                let opsi = ['tanggal', 'jenis', 'butir', 'angka', 'satuan', 'uraian_singkat'];

                _.forEach(opsi, (v) => {
                    if (v === 'angka') {
                        this.form[v] = 0.;
                    } else {
                        this.form[v] = null;
                    }
                });

                this.setTabs();
                this.isButirActive = false;
                this.opsiButir = [];
                this.$store.commit('setActiveTaskTab', this.dataActiveTabs);
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
