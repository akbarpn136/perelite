<template>
    <q-fixed-position corner="bottom-right" :offset="[18, 18]">
        <q-btn round color="green-5" small @click="onTugasClick">
            <q-icon name="add"></q-icon>
            <q-tooltip anchor="center left"
                       self="center right"
                       :offset="[20, 0]">Tambah Tugas
            </q-tooltip>
        </q-btn>
    </q-fixed-position>
</template>

<script>
    import {
        QFixedPosition,
        QBtn,
        QIcon,
        QTooltip
    } from 'quasar';

    export default {
        data() {
            return {}
        },
        components: {
            QFixedPosition,
            QBtn,
            QIcon,
            QTooltip
        },
        methods: {
            onTugasClick() {
                this.$router.push({name: 'tugas'});
            }
        }
    }
</script>

<style>
</style>
