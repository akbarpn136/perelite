<template>
    <q-tabs v-model="setActiveTask.TabName" color="deep-orange-5" align="justify">
        <q-tab name="lk" slot="title" v-if="setActiveTask.LkActive" icon="note" label="Lembar Kerja"></q-tab>
        <q-tab name="lb" slot="title" v-if="setActiveTask.LbActive" icon="history" label="Logbook"></q-tab>
        <q-tab name="tn" slot="title" v-if="setActiveTask.TnActive" icon="movie" label="Technical Note"></q-tab>
        <q-tab name="ot" slot="title" :disable="!setActiveTask.OthersActive" icon="explore" label="Lainnya"></q-tab>

        <q-tab-pane name="lk">
            <app-lk></app-lk>
        </q-tab-pane>
        <q-tab-pane name="lb">
            <app-lb></app-lb>
        </q-tab-pane>
        <q-tab-pane name="tn">
            <app-tn></app-tn>
        </q-tab-pane>
        <q-tab-pane name="ot">Konten lainnya</q-tab-pane>
    </q-tabs>
</template>

<script>
    import {
        QTabs,
        QTab,
        QTabPane,
    } from 'quasar';

    import appLk from './tugas/LembarKerja.vue';
    import appLb from './tugas/Logbook.vue';
    import appTn from './tugas/TechnicalNote.vue';
    import appOthers from './tugas/Others.vue';

    export default {
        data() {
            return {
            }
        },
        components: {
            QTabs,
            QTab,
            QTabPane,
            appLk,
            appLb,
            appTn,
            appOthers,
        },
        computed: {
            setActiveTask() {
                return this.$store.getters.getActiveTaskTab;
            }
        }
    }
</script>

<style>
</style>
