<template>
    <app-sidebar>
        <app-tasks></app-tasks>
        <router-view></router-view>
    </app-sidebar>
</template>

<script>
    import Sidebar from './shared/Sidebar.vue';
    import Tasks from './shared/Tasks.vue';

    export default {
        components: {
            appSidebar: Sidebar,
            appTasks: Tasks,
        }
    }
</script>