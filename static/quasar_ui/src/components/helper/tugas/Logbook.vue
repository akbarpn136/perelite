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
                    helper=""
                    :error="$v.judul.$error"
                    icon="build"
                    label="Judul logbook"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Judul"
                        v-model="judul"
                        type="text"
                        @blur="$v.judul.$touch(), addToTaskPackage('judul')">
                    </q-input>
                </q-field>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.unit_kerja.$error"
                    icon="build"
                    label="Unit kerja"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Unit"
                        v-model="unit_kerja"
                        type="text"
                        @blur="$v.unit_kerja.$touch(), addToTaskPackage('unit_kerja')">
                    </q-input>
                </q-field>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.pusat_kerja.$error"
                    icon="build"
                    label="Pusat kerja"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Pusat"
                        v-model="pusat_kerja"
                        type="text"
                        @blur="$v.pusat_kerja.$touch(), addToTaskPackage('pusat_kerja')">
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
                                  :options="editorOption"
                                  @blur="addToTaskPackage('uraian_lengkap')"
                                  @ready="onEditorReady($event)"
                                  style="height: 650px; margin-bottom: 68px;">
                    </quill-editor>
                </q-field>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col">
                <q-list separator>
                    <q-collapsible
                        icon="perm_identity"
                        label="Data Pemeriksa Tugas" opened>
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.nama_pemeriksa.$error"
                                    icon="info"
                                    label="Nama lengkap pemeriksa"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Nama"
                                        v-model="nama_pemeriksa"
                                        type="text"
                                        @blur="$v.nama_pemeriksa.$touch(), addToTaskPackage('nama_pemeriksa')">
                                    </q-input>
                                </q-field>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.peran_pemeriksa.$error"
                                    icon="perm data setting"
                                    label="Peran pemeriksa"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Peran"
                                        v-model="peran_pemeriksa"
                                        type="text"
                                        @blur="$v.peran_pemeriksa.$touch(), addToTaskPackage('peran_pemeriksa')">
                                    </q-input>
                                </q-field>
                            </div>
                        </div>
                    </q-collapsible>
                    <q-collapsible
                        icon="perm_identity"
                        label="Data Verifikator Tugas">
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.nama_penyetuju.$error"
                                    icon="info"
                                    label="Nama lengkap verifikator"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Nama"
                                        v-model="nama_penyetuju"
                                        type="text"
                                        @blur="$v.nama_penyetuju.$touch(), addToTaskPackage('nama_penyetuju')">
                                    </q-input>
                                </q-field>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.peran_penyetuju.$error"
                                    icon="perm data setting"
                                    label="Peran verifikator"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Peran"
                                        v-model="peran_penyetuju"
                                        type="text"
                                        @blur="$v.peran_penyetuju.$touch(), addToTaskPackage('peran_penyetuju')">
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
            this.$store.commit('setLb', {nama: 'validasi', value: this.$v});
        },

        components: {
            quillEditor,
            QField,
            QInput,
            QList,
            QCollapsible
        },
        data() {
            return {
                editorOption: {
                    debug: 'error',
                    modules: {
                        toolbar: [
                            ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                            ['blockquote', 'code-block'],

                            [{'header': 1}, {'header': 2}],               // custom button values
                            [{'list': 'ordered'}, {'list': 'bullet'}],
                            [{'script': 'sub'}, {'script': 'super'}],      // superscript/subscript
                            [{'indent': '-1'}, {'indent': '+1'}],          // outdent/indent
                            [{'direction': 'rtl'}],                         // text direction

                            [{'size': ['small', false, 'large', 'huge']}],  // custom dropdown
                            [{'header': [1, 2, 3, 4, 5, 6, false]}],

                            [{'color': []}, {'background': []}],          // dropdown with defaults from theme
                            [{'font': []}],
                            [{'align': []}],

                            ['clean'], // remove formatting button
                            ['link', 'image', 'video', 'formula'],
                            ['omega']
                        ]
                    }
                }
            }
        },
        validations: {
            nomor: {required},
            kode_peran: {required},
            judul: {required},
            unit_kerja: {required},
            pusat_kerja: {required},
            nama_pemeriksa: {required},
            peran_pemeriksa: {required},
            nama_penyetuju: {required},
            peran_penyetuju: {required},
        },
        computed: {
            nomor: {
                get() {
                    return this.$store.getters.getLbByName('nomor');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'nomor', value});
                }
            },
            judul: {
                get() {
                    return this.$store.getters.getLbByName('judul');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'judul', value});
                }
            },
            kode_peran: {
                get() {
                    return this.$store.getters.getLbByName('kode_peran');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'kode_peran', value});
                }
            },
            uraian_lengkap: {
                get() {
                    return this.$store.getters.getLbByName('uraian_lengkap');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'uraian_lengkap', value});
                }
            },
            unit_kerja: {
                get() {
                    return this.$store.getters.getLbByName('unit_kerja');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'unit_kerja', value});
                }
            },
            pusat_kerja: {
                get() {
                    return this.$store.getters.getLbByName('pusat_kerja');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'pusat_kerja', value});
                }
            },
            nama_pemeriksa: {
                get() {
                    return this.$store.getters.getLbByName('nama_pemeriksa');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'nama_pemeriksa', value});
                }
            },
            peran_pemeriksa: {
                get() {
                    return this.$store.getters.getLbByName('peran_pemeriksa');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'peran_pemeriksa', value});
                }
            },
            nama_penyetuju: {
                get() {
                    return this.$store.getters.getLbByName('nama_penyetuju');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'nama_penyetuju', value});
                }
            },
            peran_penyetuju: {
                get() {
                    return this.$store.getters.getLbByName('peran_penyetuju');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'peran_penyetuju', value});
                }
            },
        },
        methods: {
            onEditorReady(quill) {
                let toolbar = quill.getModule('toolbar');
                toolbar.addHandler('omega', function() {
                    console.log('omega')
                });

                let customButton = document.querySelector('.ql-omega');
                customButton.addEventListener('click', function() {
                  var range = quill.getSelection();
                  if (range) {
                    quill.insertText(range.index, `Kepada Yth`);
                  }
                });
            },
            addToTaskPackage(info) {
                let key = {nama: 'LOGBOOK'};
                let payload = {
                    nama: 'LOGBOOK',
                    nomor: this.nomor,
                    kode_peran: this.kode_peran,
                    judul: this.judul,
                    unit_kerja: this.unit_kerja,
                    pusat_kerja: this.pusat_kerja,
                    uraian_lengkap: this.uraian_lengkap,
                    nama_pemeriksa: this.nama_pemeriksa,
                    peran_pemeriksa: this.peran_pemeriksa,
                };

                this.$store.commit('setLb', {nama: 'validasi', value: null});
                this.$store.commit('setLb', {nama: 'validasi', value: this.$v});

                if (info !== 'uraian_lengkap') {
                    if (!this.$v[info].$error) this.$store.commit('setTaskPackages', {key, payload});
                } else {
                    this.$store.commit('setTaskPackages', {key, payload});
                }
            }
        }
    }
</script>

<style lang="sass">
    button.ql-omega:after
        content: '...'
</style>
