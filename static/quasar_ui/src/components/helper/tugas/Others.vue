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
                    :error="$v.url.$error"
                    icon="link"
                    label="Sumber URL"
                    :label-width="3"
                    :error-label="cekUrl()">
                    <q-input
                        color="secondary"
                        float-label="URL"
                        v-model="url"
                        type="text"
                        @blur="$v.url.$touch(), addToTaskPackage('url')">
                    </q-input>
                </q-field>
            </div>
        </div>
    </div>
</template>

<script>
    import {required, url} from 'vuelidate/lib/validators';
    import {
        QField,
        QInput,
        QList,
    } from 'quasar';

    export default {
        created() {
            this.$store.commit('setOt', {nama: 'validasi', value: this.$v});
        },
        components: {
            QField,
            QInput,
            QList,
        },
        validations: {
            nomor: {required},
            url: {required, url},
        },
        computed: {
            nomor: {
                get() {
                    return this.$store.getters.getOtByName('nomor');
                },
                set(value) {
                    this.$store.commit('setOt', {nama: 'nomor', value});
                }
            },
            url: {
                get() {
                    return this.$store.getters.getOtByName('url');
                },
                set(value) {
                    this.$store.commit('setOt', {nama: 'url', value});
                }
            }
        },
        methods: {
            addToTaskPackage(info) {
                let key = {nama: 'OTHERS'};
                let payload = {
                    nama: 'OTHERS',
                    nomor: this.nomor,
                    url: this.url,
                };

                this.$store.commit('setOt', {nama: 'validasi', value: null});
                this.$store.commit('setOt', {nama: 'validasi', value: this.$v});

                if (info !== 'uraian_lengkap') {
                    if (!this.$v[info].$error) this.$store.commit('setTaskPackages', {key, payload});
                } else {
                    this.$store.commit('setTaskPackages', {key, payload});
                }
            },
            cekUrl() {
                if (!this.$v.url.required) {
                    return 'URL diperlukan'
                }
                else if (!this.$v.url.url) {
                    return 'Harus dalam format URL'
                }
            }
        }
    }
</script>

<style lang="sass">
</style>
