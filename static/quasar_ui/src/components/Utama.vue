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

            <q-btn flat slot="right">
                <q-icon name="more_vert"/>
                <q-popover ref="popover" class="shadow-3">
                    <q-list link class="no-border">
                        <q-item @click="$refs.popover.close()">
                            <q-item-side icon="account circle"></q-item-side>
                            <q-item-main label="Profil"/>
                        </q-item>
                        <q-item @click="$refs.popover.close()">
                            <q-item-side icon="input"></q-item-side>
                            <q-item-main label="Masuk"/>
                        </q-item>
                    </q-list>
                </q-popover>
            </q-btn>
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

        <div class="layout-padding">
            <div class="row mb-4">
                <app-breadcrumb></app-breadcrumb>
            </div>

            <div class="row">
                <div class="col-12"> {{$store.getters.getShowModalTugas}}
                    <q-transition appear
                                  enter="bounceInDown"
                                  leave="bounceOutUp"
                                  mode="out-in">
                        <router-view :key="$route.name"/>
                    </q-transition>
                </div>
            </div>
        </div>

        <app-floating-action></app-floating-action>
        <app-modal-tugas></app-modal-tugas>
    </q-layout>
</template>

<script>
    import 'quasar-extras/animate/bounceInDown.css'
    import 'quasar-extras/animate/bounceOutUp.css'

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
        QSideLink,
        QTransition,
    } from 'quasar'

    import appBreadcrumb from './helper/Breadcrumb.vue';
    import appFloatingAction from './helper/FloatingAction.vue';
    import appModalTugas from './helper/ModalTugas.vue';

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
            QSideLink,
            QTransition,
            appBreadcrumb,
            appFloatingAction,
            appModalTugas,
        },
        data() {
            return {}
        }
    }
</script>

<style lang="sass">
    body
        background: #7474BF
        /* fallback for old browsers */
        background: -webkit-linear-gradient(to top, #348AC7, #7474BF)
        /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to top, #348AC7, #7474BF)

    .m
        &t
            margin-top: 5px
            &-1
                margin-top: 10px
            &-2
                margin-top: 15px
            &-3
                margin-top: 20px
            &-4
                margin-top: 25px
            &-5
                margin-top: 30px

        &b
            margin-bottom: 5px
            &-1
                margin-bottom: 10px
            &-2
                margin-bottom: 15px
            &-3
                margin-bottom: 20px
            &-4
                margin-bottom: 25px
            &-5
                margin-bottom: 30px

    .p
        &t
            padding-top: 5px
            &-1
                padding-top: 10px
            &-2
                padding-top: 15px
            &-3
                padding-top: 20px
            &-4
                padding-top: 25px
            &-5
                padding-top: 30px

        &b
            padding-bottom: 5px
            &-1
                padding-bottom: 10px
            &-2
                padding-bottom: 15px
            &-3
                padding-bottom: 20px
            &-4
                padding-bottom: 25px
            &-5
                padding-bottom: 30px
        &x
            padding-left: 5px
            padding-right: 5px
</style>
