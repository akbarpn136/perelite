<template>
    <nav class="navbar is-dark is-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="/">
                PereLite
            </a>

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
                    <a href="#" class="navbar-link">
                        Tugas
                    </a>

                    <div class="navbar-dropdown">
                        <a href="" class="navbar-item">
                            <span class="icon"><i class="fa fa-graduation-cap"></i></span>
                            <span class="is-uppercase">Pendidikan</span>
                        </a>

                        <a href="" class="navbar-item">
                            <span class="icon"><i class="fa fa-paper-plane"></i></span>
                            <span class="is-uppercase">Kerekayasaan</span>
                        </a>

                        <a href="" class="navbar-item">
                            <span class="icon"><i class="fa fa-briefcase"></i></span>
                            <span class="is-uppercase">Profesi</span>
                        </a>

                        <a href="" class="navbar-item">
                            <span class="icon"><i class="fa  fa-tasks"></i></span>
                            <span class="is-uppercase">Penunjang</span>
                        </a>
                    </div>
                </div>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a href="#" class="navbar-link">
                        Pengaturan
                    </a>

                    <div class="navbar-dropdown">
                        <a href="" class="navbar-item">
                            <span class="icon"><i class="fa fa-user"></i></span>
                            <span>Profil</span>
                        </a>
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