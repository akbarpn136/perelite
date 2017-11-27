<template>
    <q-modal v-model="modalStats" maximized
             :content-classes="['layout-padding', 'pt-3']">
        <h4>Form Tugas</h4>

        <div class="row md-gutter">
            <div class="col-md-4">
                <q-field
                    helper="Pilih tanggal kegiatan"
                    :error="$v.tanggal.$error"
                    error-label="Harus diisi">
                    <q-datetime
                        color="secondary"
                        float-label="Tanggal awal"
                        v-model="tanggal"
                        type="date"
                        @blur="$v.tanggal.$touch()"
                    ></q-datetime>
                </q-field>
            </div>
            <div class="col-md-4">
                <q-field
                    helper=""
                    :error="$v.jenis.$error"
                    error-label="Harus diisi">
                    <q-select
                        color="secondary"
                        float-label="Kategori Tugas"
                        v-model="jenis"
                        :options="opsiJenis"
                        @blur="$v.jenis.$touch()"
                        @change="onSelectKategoriChange"
                    ></q-select>
                </q-field>
            </div>
            <div class="col-md-4">
                <q-field
                    helper=""
                    :error="$v.butir.$error"
                    error-label="Harus diisi">
                    <q-select
                        color="secondary"
                        float-label="Butir Tugas"
                        v-model="butir"
                        :options="opsiButir"
                        :filter="true"
                        @blur="$v.butir.$touch()"
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
                    :error="$v.angka.$error"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Angka"
                        v-model="angka"
                        type="number"
                        readonly disable :before="[
                            {icon: 'filter 9 plus', content: true}
                        ]"
                        @blur="$v.angka.$touch()"
                    ></q-input>
                </q-field>
            </div>
            <div class="col-md-6">
                <q-field
                    helper="Satuan: LK, LB, TN, Lainnya"
                    :error="$v.satuan.$error"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Satuan Hasil"
                        v-model="satuan"
                        type="text"
                        readonly disable :before="[
                            {icon: 'insert drive file', content: true}
                        ]"
                        @blur="$v.satuan.$touch()"
                    ></q-input>
                </q-field>
            </div>
        </div>

        <div class="row md-gutter">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.uraian_singkat.$error"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Uraian Singkat"
                        v-model="uraian_singkat"
                        type="textarea"
                        @blur="$v.uraian_singkat.$touch()"
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
        QSelect,
        Toast
    } from 'quasar';

    import appTabsTugas from './TabsTugas.vue';
    import {GetButir} from '../../http/butir';

    export default {
        data() {
            return {
                koleksiButir: null,
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
            tanggal: {required},
            jenis: {required},
            butir: {required},
            angka: {required},
            satuan: {required},
            uraian_singkat: {required}
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
                _.forEach(this.$store.getters.getTugasByName(), (v, k) => {
                    if (k !== 'taskPackages') {
                        this.$v[k].$reset();
                    }
                });
                this.$store.commit('setShowModalTugas', false);
                this.clearForm();
            },
            onSelectKategoriChange() {
                if (!this.isButirActive) {
                    this.isButirActive = true;
                }
                this.opsiButir = [];
                this.onGetButir(this.jenis);
            },
            onSelectButirChange() {
                const selectedButir = _.filter(this.koleksiButir, (el) => {
                    return (el.butir === this.butir);
                });

                this.angka = selectedButir[0].angka;
                this.satuan = selectedButir[0].hasil;
                this.checkActiveTabs(this.satuan);
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
                        this.$store.commit('setTugas', {nama: v, value: 0.});
                    } else {
                        this.$store.commit('setTugas', {nama: v, value: null});
                    }
                });

                this.setTabs();
                this.isButirActive = false;
                this.opsiButir = [];
                this.$store.commit('setActiveTaskTab', this.dataActiveTabs);
            },
            onFormTugasSubmit() {
                let obj = this.$store.getters.getTugasByName();

                let paketTugas = this.$store.getters.getTaskPackages;

                if (_.isEmpty(paketTugas)) {
                    Toast.create.negative('Minimal ada satu paket tugas, misal: LK');
                }
            }
        },
        computed: {
            modalStats() {
                return this.$store.getters.getShowModalTugas;
            },
            tanggal: {
                get() {
                    return this.$store.getters.getTugasByName('tanggal');
                },
                set(value) {
                    this.$store.commit('setTugas', {nama: 'tanggal', value});
                }
            },
            jenis: {
                get() {
                    return this.$store.getters.getTugasByName('jenis');
                },
                set(value) {
                    this.$store.commit('setTugas', {nama: 'jenis', value});
                }
            },
            butir: {
                get() {
                    return this.$store.getters.getTugasByName('butir');
                },
                set(value) {
                    this.$store.commit('setTugas', {nama: 'butir', value});
                }
            },
            angka: {
                get() {
                    return this.$store.getters.getTugasByName('angka');
                },
                set(value) {
                    this.$store.commit('setTugas', {nama: 'angka', value});
                }
            },
            satuan: {
                get() {
                    return this.$store.getters.getTugasByName('satuan');
                },
                set(value) {
                    this.$store.commit('setTugas', {nama: 'satuan', value});
                }
            },
            uraian_singkat: {
                get() {
                    return this.$store.getters.getTugasByName('uraian_singkat');
                },
                set(value) {
                    this.$store.commit('setTugas', {nama: 'uraian_singkat', value});
                }
            }
        }
    }
</script>

<style>
</style>
