<template>
    <q-list no-border class="bg-white col-12 no-padding shadow-4">
        <q-item>
            <q-item-side>Lokasi: </q-item-side>
            <q-item-main>
                <ul class="breadcrumb">
                    <li v-for="(r, i) in $route.matched" :key="i">
                        <router-link :to="{name: r.name}">
                            <q-icon name="home" v-if="r.name === 'utama'"></q-icon>
                            <span :class="{'xs-hide': r.name === 'utama'}">{{r.name | capitalize | splitString}}</span>
                        </router-link>
                    </li>
                </ul>
            </q-item-main>
        </q-item>
    </q-list>
</template>

<script>
    import {
        QIcon,
        QList,
        QItem,
        QItemSide,
        QItemMain
    } from 'quasar';

    export default {
        data() {
            return {}
        },
        components: {
            QIcon,
            QList,
            QItem,
            QItemSide,
            QItemMain
        },
        filters: {
            capitalize: function (value) {
                if (!value) return '';
                value = value.toString();
                return value.charAt(0).toUpperCase() + value.slice(1);
            },
            splitString: function (value) {
                return value.replace(/([A-Z]+)/g, " $1").replace(/([A-Z][a-z])/g, " $1");
            }
        }
    }
</script>

<style>
</style>
