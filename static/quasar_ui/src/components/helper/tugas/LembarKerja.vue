<template>
    <div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.lk.nomor.$error"
                    icon="format list numbered"
                    label="Nomor tugas"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Penomoran"
                        v-model="lk.nomor"
                        type="text"
                        @blur="$v.lk.nomor.$touch()">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.lk.referensi.$error"
                    icon="link"
                    label="Referensi tugas"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Referensi"
                        v-model="lk.referensi"
                        type="text"
                        @blur="$v.lk.referensi.$touch()">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper="misal: Leader 2, Engineering Staff 2.4"
                    :error="$v.lk.kode_peran.$error"
                    icon="code"
                    label="Peran dalam kerekayasaan"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Peran"
                        v-model="lk.kode_peran"
                        type="text"
                        @blur="$v.lk.kode_peran.$touch()">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper="misal: disain & programming"
                    :error="$v.lk.wbs_wp.$error"
                    icon="movie"
                    label="WBS/WP"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Kelompok"
                        v-model="lk.wbs_wp"
                        type="text"
                        @blur="$v.lk.wbs_wp.$touch()">
                    </q-input>
                </q-field>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.lk.program.$error"
                    icon="build"
                    label="Nama program"
                    :label-width="3"
                    error-label="Harus diisi">
                    <q-input
                        color="secondary"
                        float-label="Program"
                        v-model="lk.program"
                        type="text"
                        @blur="$v.lk.program.$touch()">
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
                    <quill-editor v-model="lk.uraian_lengkap"
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
                                    :error="$v.lk.nama_pemberi.$error"
                                    icon="info"
                                    label="Nama lengkap pemberi"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Nama"
                                        v-model="lk.nama_pemberi"
                                        type="text"
                                        @blur="$v.lk.nama_pemberi.$touch()">
                                    </q-input>
                                </q-field>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <q-field
                                    helper=""
                                    :error="$v.lk.peran_pemberi.$error"
                                    icon="perm data setting"
                                    label="Peran pemberi"
                                    :label-width="3"
                                    error-label="Harus diisi">
                                    <q-input
                                        color="secondary"
                                        float-label="Peran"
                                        v-model="lk.peran_pemberi"
                                        type="text"
                                        @blur="$v.lk.peran_pemberi.$touch()">
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
        data() {
            return {
                lk: {
                    nama: 'LEMBAR KERJA',
                    kode_peran: null,
                    nomor: null,
                    referensi: null,
                    program: null,
                    wbs_wp: null,
                    uraian_lengkap: null,
                    nama_pemberi: null,
                    peran_pemberi: null
                }
            }
        },
        components: {
            quillEditor,
            QField,
            QInput,
            QList,
            QCollapsible
        },
        validations: {
            lk: {
                nama: {required},
                kode_peran: {required},
                nomor: {required},
                referensi: {required},
                program: {required},
                wbs_wp: {required},
                uraian_lengkap: {required},
                nama_pemberi: {required},
                peran_pemberi: {required}
            }
        }
    }
</script>

<style>
</style>
