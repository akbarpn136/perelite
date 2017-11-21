<template>
    <q-modal v-model="modalStats" maximized :content-classes="['layout-padding', 'pt-3']">
        <h4>Basic Modal</h4>
        <q-btn color="primary"
               @click="onModalClose">
            Close
        </q-btn>
    </q-modal>
</template>

<script>
    import {
        QBtn,
        QModal
    } from 'quasar';

    export default {
        data() {
            return {}
        },
        components: {
            QBtn,
            QModal
        },
        methods: {
            onModalClose() {
                this.$store.commit('setShowModalTugas', false);
            }
        },
        computed: {
            modalStats() {
                return this.$store.getters.getShowModalTugas;
            }
        }
    }
</script>

<style>
</style>
