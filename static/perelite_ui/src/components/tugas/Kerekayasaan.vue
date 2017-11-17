<template>
    <app-sidebar>
        <router-view></router-view>
        <app-tasks v-if="isParent"></app-tasks>
    </app-sidebar>
</template>

<script>
    import Sidebar from './shared/Sidebar.vue';
    import Tasks from './shared/Tasks.vue';

    export default {
        components: {
            appSidebar: Sidebar,
            appTasks: Tasks,
        },
        computed: {
            isParent() {
                return this.$store.getters.getShowParent;
            }
        },
        beforeRouteUpdate(to, from, next) {
            if (to.name === 'pendidikan') {
                this.$store.commit('setShowParent', true);
            }

            else {
                this.$store.commit('setShowParent', false);
            }
            next();
        }
    }
</script>