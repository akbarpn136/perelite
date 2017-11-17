<template>
    <div class="box">
        <nav class="level">
            <!-- Left side -->
            <div class="level-left">
                <div class="level-item">
                    <nav class="breadcrumb has-arrow-separator" aria-label="breadcrumbs">
                        <ul><span class="tag is-info">Lokasi:</span>
                            <li>
                                <router-link to="utama">Utama</router-link>
                            </li>
                            <router-link :to="r.path"
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

            <!-- Right side -->
            <div class="level-right">
                <div class="level-item">
                    <nav class="pagination" role="navigation" aria-label="pagination">
                        <a class="pagination-previous">
                            <span class="icon"><i class="fa fa-angle-left"></i></span>
                        </a>
                        <a class="pagination-next">
                            <span class="icon"><i class="fa fa-angle-right"></i></span>
                        </a>
                        <ul class="pagination-list">
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