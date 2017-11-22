<template>
    <div>
        <div class="row">
            <div class="col">
                <q-field
                    helper=""
                    :error="$v.lk.nomor.$error"
                    icon="format list numbered"
                    label="Nomor Tugas"
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
                    label="Referensi Tugas"
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
                    helper="misal: L 2, ES 2.4"
                    :error="$v.lk.kode_peran.$error"
                    icon="code"
                    label="Kode Peran"
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
                    label="Nama Program"
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
                    <vue-editor v-model="lk.uraian_lengkap"
                                @blur="$v.lk.uraian_lengkap.$touch()"
                                id="lk" style="height: 650px;"></vue-editor>
                </q-field>
            </div>
        </div>
    </div>
</template>

<script>
    import {required} from 'vuelidate/lib/validators';
    import { VueEditor } from 'vue2-quill-editor'
    import {
        QField,
        QInput
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
                    uraian_lengkap: null
                }
            }
        },
        components: {
            QField,
            QInput,
            VueEditor
        },
        validations: {
            lk: {
                nama: {required},
                kode_peran: {required},
                nomor: {required},
                referensi: {required},
                program: {required},
                wbs_wp: {required},
                uraian_lengkap: {required}
            }
        }
    }
</script>

<style>
</style>
