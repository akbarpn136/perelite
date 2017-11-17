<template>
    <div class="card">
        <header class="card-header">
            <div class="card-header-title level">
                <app-filter-task></app-filter-task>
            </div>
        </header>

        <div class="card-content">
            <table class="table is-hoverable is-fullwidth">
                <thead>
                <tr>
                    <th>#</th>
                    <th>Butir</th>
                    <th>Uraian Kegiatan</th>
                    <th class="has-text-centered">Pilihan</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="baris in 10"
                    :key="baris">
                    <th>{{baris}}</th>
                    <td>
                        Butir {{baris}}
                    </td>
                    <td>
                        Qualification for the
                        <a title="2016–17 UEFA Champions League">
                            Champions League group stage
                        </a>
                    </td>
                    <td>
                        <div class="buttons is-centered">
                            <span class="button is-small" title="Duplikat dokumen">
                                <span class="icon"><i class="fa fa-copy"></i></span>
                            </span>
                            <span class="button is-small" title="Ubah dokumen">
                                <span class="icon"><i class="fa fa-pencil"></i></span>
                            </span>
                            <span class="button is-small" title="Rincian dokumen">
                                <span class="icon"><i class="fa fa-eye"></i></span>
                            </span>
                        </div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    import FilterTask from './FilterTask.vue';

    export default {
        components: {
            appFilterTask: FilterTask
        }
    }
</script>