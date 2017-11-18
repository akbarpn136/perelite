<template>
    <div>
        <div class="box is-radiusless" v-if="isParent" :key="$route.path">Something good.</div>
        <transition enterActiveClass="animated slideInRight"
                    leaveActiveClass="animated slideOutRight"
                    mode="out-in"
                    duration="650">
            <router-view :key="$route.path"></router-view>
        </transition>
    </div>
</template>

<script>
    import Sidebar from './tugas/shared/Sidebar.vue';

    export default {
        components: {
            appSidebar: Sidebar,
        },
        computed: {
            isParent() {
                return this.$store.getters.getShowParent;
            }
        },
        created() {
            this.$store.commit('setShowParent', true);
        },
        beforeRouteUpdate(to, from, next) {
            if (to.name === 'utama') {
                this.$store.commit('setShowParent', true);
            }

            else {
                this.$store.commit('setShowParent', false);
            }
            next();
        }
    }
</script>