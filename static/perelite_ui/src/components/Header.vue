<template>
    <nav class="navbar is-dark is-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <router-link to="utama"
                    class="navbar-item" exact>PereLite</router-link>

            <div class="navbar-burger"
                 :class="{'is-active': isActive}" @click="onBurgerClick">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div class="navbar-menu"
             :class="{'is-active': isActive}">
            <div class="navbar-end">
                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        Tugas
                    </a>

                    <div class="navbar-dropdown">
                        <router-link to="pendidikan"
                                     class="navbar-item"
                                     exact-active-class="is-active">
                            <span class="icon"><i class="fa fa-graduation-cap"></i></span>
                            <span class="is-uppercase">Pendidikan</span>
                        </router-link>

                        <router-link to="kerekayasaan"
                                     class="navbar-item"
                                     exact-active-class="is-active">
                            <span class="icon"><i class="fa fa-paper-plane"></i></span>
                            <span class="is-uppercase">Kerekayasaan</span>
                        </router-link>

                        <router-link to="profesi"
                                     class="navbar-item"
                                     exact-active-class="is-active">
                            <span class="icon"><i class="fa fa-briefcase"></i></span>
                            <span class="is-uppercase">Profesi</span>
                        </router-link>

                        <router-link to="penunjang"
                                     class="navbar-item"
                                     exact-active-class="is-active">
                            <span class="icon"><i class="fa  fa-tasks"></i></span>
                            <span class="is-uppercase">Penunjang</span>
                        </router-link>
                    </div>
                </div>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        Pengaturan
                    </a>

                    <div class="navbar-dropdown">
                        <router-link to="profil"
                                     class="navbar-item"
                                     exact-active-class="is-active">
                            <span class="icon"><i class="fa fa-user"></i></span>
                            <span class="is-uppercase">Profil</span>
                        </router-link>
                        <a href="" class="navbar-item">
                            <span class="icon"><i class="fa fa-sign-in"></i></span>
                            <span>Masuk</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        data() {
            return {
                isActive: false
            }
        },
        methods: {
            onBurgerClick() {
                this.isActive = !this.isActive;
            }
        }
    }
</script>
<style></style>