<template>
    <div>
        <app-header></app-header>
        <div class="section">
            <div class="container is-fluid is-marginless">
                <transition enterActiveClass="animated fadeInDown"
                            mode="out-in"
                            appear>
                    <router-view></router-view>
                </transition>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from './components/Header.vue'

    export default {
        components: {
            appHeader: Header
        }
    }
</script>

<style>
</style>
