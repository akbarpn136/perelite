<template>
    <div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.nomor.$error"
                    icon="format list numbered"
                    label="Nomor tugas"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Penomoran"
                        v-model="nomor"
                        type="text"
                        @blur="$v.nomor.$touch(), addToTaskPackage('nomor')">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.referensi.$error"
                    icon="link"
                    label="Referensi tugas"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Referensi"
                        v-model="referensi"
                        type="text"
                        @blur="$v.referensi.$touch(), addToTaskPackage('referensi')">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper="misal: Leader 2, Engineering Staff 2.4"
                    :error="$v.kode_peran.$error"
                    icon="code"
                    label="Peran dalam kerekayasaan"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Peran"
                        v-model="kode_peran"
                        type="text"
                        @blur="$v.kode_peran.$touch(), addToTaskPackage('kode_peran')">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper="misal: disain & programming"
                    :error="$v.wbs_wp.$error"
                    icon="movie"
                    label="WBS/WP"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Kelompok"
                        v-model="wbs_wp"
                        type="text"
                        @blur="$v.wbs_wp.$touch(), addToTaskPackage('wbs_wp')">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.program.$error"
                    icon="build"
                    label="Nama program"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Program"
                        v-model="program"
                        type="text"
                        @blur="$v.program.$touch(), addToTaskPackage('program')">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper="Uraian lengkap"
                    :error="false"
                    error-label="Harus diisi">
                    <quill-editor v-model="uraian_lengkap"
                                  @blur="addToTaskPackage('uraian_lengkap')"
                                  style="height: 650px; margin-bottom: 68px;"
                                  ref="lk">
                    </quill-editor>
                </q-field>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col">
                <q-list separator>
                    <q-collapsible
                        icon="perm_identity"
                        label="Data Pemberi Tugas" opened>
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.nama_pemberi.$error"
                                    icon="info"
                                    label="Nama lengkap pemberi"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Nama"
                                        v-model="nama_pemberi"
                                        type="text"
                                        @blur="$v.nama_pemberi.$touch(), addToTaskPackage('nama_pemberi')">
                                    </q-input>
                                </q-field>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.peran_pemberi.$error"
                                    icon="perm data setting"
                                    label="Peran pemberi"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Peran"
                                        v-model="peran_pemberi"
                                        type="text"
                                        @blur="$v.peran_pemberi.$touch(), addToTaskPackage('peran_pemberi')">
                                    </q-input>
                                </q-field>
                            </div>
                        </div>
                    </q-collapsible>
                </q-list>
            </div>
        </div>
    </div>
</template>

<script>
    import {required} from 'vuelidate/lib/validators';
    import {quillEditor} from 'vue-quill-editor'
    import {
        QField,
        QInput,
        QList,
        QCollapsible
    } from 'quasar';

    export default {
        created() {
            this.$store.commit('setLk', {nama:'validasi', value: this.$v});
        },
        components: {
            quillEditor,
            QField,
            QInput,
            QList,
            QCollapsible
        },
        validations: {
            kode_peran: {required},
            nomor: {required},
            referensi: {required},
            program: {required},
            wbs_wp: {required},
            nama_pemberi: {required},
            peran_pemberi: {required}
        },
        computed: {
            kode_peran: {
                get() {
                    return this.$store.getters.getLkByName('kode_peran');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'kode_peran', value});
                }
            },
            nomor: {
                get() {
                    return this.$store.getters.getLkByName('nomor');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'nomor', value});
                }
            },
            referensi: {
                get() {
                    return this.$store.getters.getLkByName('referensi');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'referensi', value});
                }
            },
            program: {
                get() {
                    return this.$store.getters.getLkByName('program');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'program', value});
                }
            },
            wbs_wp: {
                get() {
                    return this.$store.getters.getLkByName('wbs_wp');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'wbs_wp', value});
                }
            },
            uraian_lengkap: {
                get() {
                    return this.$store.getters.getLkByName('uraian_lengkap');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'uraian_lengkap', value});
                }
            },
            nama_pemberi: {
                get() {
                    return this.$store.getters.getLkByName('nama_pemberi');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'nama_pemberi', value});
                }
            },
            peran_pemberi: {
                get() {
                    return this.$store.getters.getLkByName('peran_pemberi');
                },
                set(value) {
                    this.$store.commit('setLk', {nama: 'peran_pemberi', value});
                }
            },
        },
        methods: {
            addToTaskPackage(info) {
                let key = {nama: 'LEMBAR KERJA'};
                let payload = {
                    nama: 'LEMBAR KERJA',
                    kode_peran: this.kode_peran,
                    nomor: this.nomor,
                    referensi: this.referensi,
                    program: this.program,
                    wbs_wp: this.wbs_wp,
                    uraian_lengkap: this.uraian_lengkap,
                    nama_pemberi: this.nama_pemberi,
                    peran_pemberi: this.peran_pemberi,
                };

                this.$store.commit('setLk', {nama:'validasi', value: null});
                this.$store.commit('setLk', {nama:'validasi', value: this.$v});

                if (info !== 'uraian_lengkap' && !this.$v[info].$error) {
                    this.$store.commit('setTaskPackages', {key, payload});
                }
            }
        }
    }
</script>

<style>
</style>
