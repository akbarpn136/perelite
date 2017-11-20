<template>
    <q-layout
        ref="layout"
        view="hHh Lpr fff"
        :left-class="{'bg-grey-2': true}">
        <q-toolbar slot="header" color="dark">
            <q-btn
                flat
                @click="$refs.layout.toggleLeft()">
                <q-icon name="menu"/>
            </q-btn>

            <q-toolbar-title>
                <q-side-link tag="a"
                             :to="{name: 'utama'}"
                             class="text-white">
                    PereLite
                </q-side-link>
            </q-toolbar-title>

            <q-icon slot="right" name="more_vert">
                <q-popover ref="popover" class="shadow-1">
                    <q-list link class="no-border">
                        <q-item @click="$refs.popover.close()">
                            <q-item-side icon="alarm" right></q-item-side>
                            <q-item-main label="Profil"/>
                        </q-item>
                        <q-item @click="$refs.popover.close()">
                            <q-item-side icon="input" right></q-item-side>
                            <q-item-main label="Masuk"/>
                        </q-item>
                    </q-list>
                </q-popover>
            </q-icon>
        </q-toolbar>

        <div slot="left">
            <q-list no-border inset-delimiter>
                <q-list-header>Utama</q-list-header>
                <q-side-link item :to="{name: 'pendidikan'}">
                    <q-item-side icon="school"/>
                    <q-item-main label="Pendidikan"
                                 sublabel="Mengikuti pendidikan & pelatihan"/>
                </q-side-link>
                <q-side-link item :to="{name: 'kerekayasaan'}">
                    <q-item-side icon="flight"/>
                    <q-item-main label="Kerekayasaan"
                                 sublabel="Melakukan kegiatan kerekayasaan"/>
                </q-side-link>
                <q-side-link item :to="{name: 'profesi'}">
                    <q-item-side icon="work"/>
                    <q-item-main label="Profesi"
                                 sublabel="Melakukan pengembangan profesi"/>
                </q-side-link>
                <q-side-link item :to="{name: 'penunjang'}">
                    <q-item-side icon="trending up"/>
                    <q-item-main label="Penunjang"
                                 sublabel="Melakukan kegiatan penunjang"/>
                </q-side-link>

                <q-item-separator></q-item-separator>

                <q-list-header>Surat Pernyataan</q-list-header>
                <q-item>
                    <q-field class="full-width"
                             helper="Jenis tugas"
                             error-label="We need a valid email">
                        <q-select
                            stack-label="Kategori"
                            color="secondary"
                            separator
                            v-model="jenis"
                            :options="options"/>
                    </q-field>
                </q-item>
                <q-item>
                    <q-field class="full-width"
                             helper=""
                             error-label="Tidak boleh kosong">
                        <q-datetime stack-label="Tanggal Awal"
                                    v-model="tglAwal"
                                    type="date"/>
                    </q-field>
                </q-item>
                <q-item>
                    <q-field class="full-width"
                             helper=""
                             error-label="Tidak boleh kosong">
                        <q-datetime stack-label="Tanggal Akhir"
                                    v-model="tglAkhir"
                                    type="date"/>
                    </q-field>
                </q-item>
                <q-item>
                    <q-btn loader
                           color="primary"
                           class="full-width"
                           @click="onButtonProsesClick">
                        PROSES
                        <span slot="loading">
                            <q-spinner-puff class="on-left"></q-spinner-puff>
                            PROSES
                        </span>
                    </q-btn>
                </q-item>
            </q-list>
        </div>

        lalal
        <router-view key="komponen"/>
    </q-layout>
</template>

<script>
    import {required} from 'vuelidate/lib/validators'
    import {
        QLayout,
        QToolbar,
        QToolbarTitle,
        QBtn,
        QIcon,
        QList,
        QListHeader,
        QItemSeparator,
        QItem,
        QItemSide,
        QItemMain,
        QPopover,
        QInput,
        QSelect,
        QField,
        QSideLink,
        QDatetime,
        QSpinnerPuff
    } from 'quasar'

    export default {
        name: 'index',
        components: {
            QLayout,
            QToolbar,
            QToolbarTitle,
            QBtn,
            QIcon,
            QList,
            QListHeader,
            QItemSeparator,
            QItem,
            QItemSide,
            QItemMain,
            QPopover,
            QInput,
            QSelect,
            QField,
            QSideLink,
            QDatetime,
            QSpinnerPuff
        },
        data() {
            return {
                jenis: '',
                tglAwal: '',
                tglAkhir: '',
                options: [
                    {label: 'Pendidikan', value: 'Pendidikan'},
                    {label: 'Kerekayasaan', value: 'Kerekayasaan'},
                    {label: 'Profesi', value: 'Profesi'},
                    {label: 'Penunjang', value: 'Penunjang'},
                ]
            }
        },
        validations: {},
        computed: {},
        methods: {
            onButtonProsesClick(event, done) {
                const obj = {
                    'jenis': this.jenis,
                    'tglAwal': this.tglAwal,
                    'tglAkhir': this.tglAkhir,
                }
                setTimeout(() => {
                    console.log(obj);
                    done();
                }, 2000)
            }
        }
    }
</script>

<style lang="stylus">
</style>
