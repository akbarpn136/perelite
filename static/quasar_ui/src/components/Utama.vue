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
            <q-list no-border>
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

                <q-list-header>Pendukung</q-list-header>
                <q-side-link item :to="{name: 'pernyataan'}">
                    <q-item-side icon="receipt"/>
                    <q-item-main label="Pernyataan"
                                 sublabel="Lihat surat pernyataan"/>
                </q-side-link>
            </q-list>
        </div>

        <router-view key="komponen"/>
    </q-layout>
</template>

<script>
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
        QSideLink
    } from 'quasar'

    export default {
        name: 'utama',
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
            QSideLink
        },
        data() {
            return {

            }
        },
        computed: {}
    }
</script>

<style lang="stylus">
</style>
