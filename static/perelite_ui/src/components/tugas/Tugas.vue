<template>
    <app-tasks></app-tasks>
</template>

<script>
    import Sidebar from './shared/Sidebar.vue';
    import Tasks from './shared/Tasks.vue';

    export default {
        components: {
            appSidebar: Sidebar,
            appTasks: Tasks,
        },
        created() {
            this.$store.commit('setShowParent', false);
        }
    }
</script>