<template>
    <div class="layout-padding bg-white">
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
                       @click="onFormTugasSubmit()"
                       icon="save">
                    Simpan
                </q-btn>
                <q-btn color="grey-5"
                       @click="onBatalClick()"
                       icon="not interested">
                    Batal
                </q-btn>
            </div>
        </div>
    </div>
</template>

<script>
    import * as _ from 'lodash';
    import {required} from 'vuelidate/lib/validators';
    import {
        QBtn,
        QField,
        QInput,
        QDatetime,
        QSelect,
        Toast
    } from 'quasar';

    import appTabsTugas from './TabsTugas.vue';
    import {GetButir} from '../../http/butir';
    import {TambahTugas, LihatTugasTertentu, UbahTugasTertentu} from '../../http/tugas';

    export default {
        data() {
            return {
                mode: null,
                opsi: ['tanggal', 'jenis', 'butir', 'angka', 'satuan', 'uraian_singkat'],
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
            QField,
            QInput,
            QDatetime,
            QSelect,
            appTabsTugas
        },
        created() {
            let pk = this.$route.params['pk'];
            if (pk) {
                this.mode = (this.$route.name === 'duplikatTugas') ? 'tambah': 'ubah';
                LihatTugasTertentu(pk).then(res => {
                    this.tanggal = res.data.tanggal.$date;
                    this.jenis = res.data.kategori;
                    this.butir = res.data.butir;
                    this.angka = res.data.angka;
                    this.satuan = res.data.satuan;
                    this.uraian_singkat = res.data.uraian_singkat;
                    this.checkActiveTabs(this.satuan);
                    this.onGetButir(this.jenis);
                    this.isButirActive = !this.isButirActive;
                    this.assignTaskPackages(res.data['paket_tugas']);
                    this.$store.commit('clearTaskPackages');
                    _.forEach(res.data['paket_tugas'], v => {
                        this.$store.commit('setTaskPackages', {
                            key: {nama: v.nama},
                            payload: v
                        });
                    });
                }).catch(err => {
                    console.log(err);
                });
            } else {
                this.mode = 'tambah';
            }
        },
        methods: {
            assignTaskPackages(data) {
                const lk = data.filter(el => {
                    return el.nama === 'LEMBAR KERJA';
                });
                const lb = data.filter(el => {
                    return el.nama === 'LOGBOOK';
                });
                const tn = data.filter(el => {
                    return el.nama === 'TECHNICAL NOTE';
                });

                if (lk.length > 0) {
                    _.forEach(lk[0], (v, k) => {
                        this.$store.commit('setLk', {nama: k, value: v});
                    });
                }

                if (lb.length > 0) {
                    _.forEach(lb[0], (v, k) => {
                        this.$store.commit('setLb', {nama: k, value: v});
                    });
                }

                if (tn.length > 0) {
                    _.forEach(tn[0], (v, k) => {
                        this.$store.commit('setTn', {nama: k, value: v});
                    });
                }
            },
            onBatalClick() {
                this.$v.$reset();
                this.clearForm();
                this.$router.go(-1);
            },
            onSelectKategoriChange() {
                if (!this.isButirActive) {
                    this.isButirActive = true;
                }
                this.opsiButir = [];
                this.clearTaskPackage();
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
            setTabs(TabName = null,
                    LkActive = false,
                    LbActive = false,
                    TnActive = false,
                    OthersActive = false) {
                let opsi = {TabName, LkActive, LbActive, TnActive, OthersActive};

                _.forEach(opsi, (v, k) => {
                    this.dataActiveTabs[k] = v;
                });
            },
            clearForm() {
                _.forEach(this.opsi, (v) => {
                    if (v === 'angka') {
                        this.$store.commit('setTugas', {nama: v, value: 0.});
                    } else {
                        this.$store.commit('setTugas', {nama: v, value: null});
                    }
                });

                this.setTabs();
                this.clearTaskPackage();
                this.isButirActive = false;
                this.opsiButir = [];
                this.$store.commit('setActiveTaskTab', this.dataActiveTabs);
            },
            clearTaskPackage() {
                this.$store.commit('clearTaskPackages');
                let lk = this.$store.getters.getLkByName();
                let lb = this.$store.getters.getLbByName();
                let tn = this.$store.getters.getTnByName();
                _.forEach(lk, (v, k) => {
                    if (v !== 'LEMBAR KERJA') {
                        this.$store.commit('setLk', {nama: k, value: null});
                    }
                });
                _.forEach(lb, (v, k) => {
                    if (v !== 'LOGBOOK') {
                        this.$store.commit('setLb', {nama: k, value: null});
                    }
                });
                _.forEach(tn, (v, k) => {
                    if (v !== 'TECHNICAL NOTE') {
                        this.$store.commit('setLb', {nama: k, value: null});
                    }
                });
            },
            onFormTugasSubmit() {
                let obj = this.$store.getters.getTugasByName();
                let paketTugas = this.$store.getters.getTaskPackages;
                let validasiLk = this.$store.getters.getLkByName('validasi');
                let validasiLb = this.$store.getters.getLbByName('validasi');
                let validasiTn = this.$store.getters.getTnByName('validasi');

                this.$v.$touch();
                if (validasiLk) validasiLk.$touch();
                if (validasiLb) validasiLb.$touch();
                if (validasiTn) validasiTn.$touch();

                if (!this.$v.$invalid) {
                    let paket = [];
                    _.forEach(obj.taskPackages, (v) => {
                        paket.push(JSON.stringify(v));
                    });

                    let payload = new FormData();
                    payload.append('tanggal', new Date(obj.tanggal).toLocaleDateString());
                    payload.append('kategori', obj.jenis);
                    payload.append('butir', obj.butir);
                    payload.append('angka', obj.angka);
                    payload.append('satuan', obj.satuan);
                    payload.append('uraian_singkat', obj.uraian_singkat);
                    payload.append('paket_tugas', JSON.stringify(paket));

                    if (this.mode === 'tambah') {
                        TambahTugas(payload).then((res) => {
                            Toast.create.positive('Tugas berhasil disimpan.');
                            this.$router.push({name: this.jenis});
                            this.clearForm();
                        }).catch((err) => {
                            _.forEach(err.response.data, (v, k) => {
                                if (k === 'paket_tugas') {
                                    Toast.create.negative('Masing-masing input paket tugas harus diisi');
                                }
                                else {
                                    Toast.create.negative(`${k}: ${v}`);
                                }
                            });
                        });
                    } else {
                        // Ubah tugas is here...
                        UbahTugasTertentu(this.$route.params['pk'], payload).then((res) => {
                            Toast.create.positive('Tugas berhasil disimpan.');
                            this.$router.push({name: this.jenis});
                            this.clearForm();
                        }).catch((err) => {
                            _.forEach(err.response.data, (v, k) => {
                                Toast.create.negative(`${k}: ${v}`);
                            });
                        });
                    }

                } else {
                    Toast.create.negative('Perbaiki kesalahan yang terjadi.');
                }
            }
        },
        computed: {
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
