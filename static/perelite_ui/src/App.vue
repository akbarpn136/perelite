<template>
    <div>
        <app-header></app-header>
        <div class="section">
            <div class="container is-fluid is-marginless">
                <app-sidebar>
                    <router-view></router-view>
                </app-sidebar>
                <router-view name="outer"></router-view>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from './components/Header.vue';
    import Sidebar from './components/tugas/shared/Sidebar.vue';

    export default {
        components: {
            appHeader: Header,
            appSidebar: Sidebar,
        }
    }
</script>

<style>
</style>
