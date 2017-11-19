<template>
    <div class="box is-paddingless-y is-radiusless">
        <nav class="level">
            <!-- Left side -->
            <div class="level-left">
                <div class="level-item">
                    <nav class="breadcrumb has-arrow-separator" aria-label="breadcrumbs">
                        <ul><span class="tag is-primary"><i class="fa fa-map-marker"></i></span>
                            <router-link :to="{name: r.name}"
                                         tag="li"
                                         v-for="r in $route.matched"
                                         :key="r.name"
                                         exact-active-class="is-active">
                                <a>{{r.name | splitString | capitalize}}</a>
                            </router-link>
                        </ul>
                    </nav>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
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

<style scoped>
    .box {
        padding-top: 4px;
        padding-bottom: 4px;
    }
</style>