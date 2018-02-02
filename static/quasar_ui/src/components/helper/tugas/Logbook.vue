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
            nama_pemberi: {required},
            peran_pemberi: {required}
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
            nama_pemberi: {
                get() {
                    return this.$store.getters.getLbByName('nama_pemberi');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'nama_pemberi', value});
                }
            },
            peran_pemberi: {
                get() {
                    return this.$store.getters.getLbByName('peran_pemberi');
                },
                set(value) {
                    this.$store.commit('setLb', {nama: 'peran_pemberi', value});
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
                    nama_pemberi: this.nama_pemberi,
                    peran_pemberi: this.peran_pemberi,
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
