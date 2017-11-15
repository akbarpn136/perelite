<template>
    <div class="columns">
        <div class="column is-one-fifth">
            <div class="box">
                <h3 class="subtitle is-5">Masih kurang?</h3>
                <button class="button is-primary is-fullwidth">
                    <span class="icon"><i class="fa fa-plus-circle"></i></span>
                    <span>Tambah</span>
                </button>
            </div>

            <div class="card">
                <header class="card-header">
                    <p class="card-header-title">
                        Surat Pernyataan
                    </p>
                </header>
                <div class="card-content">
                    <div class="content">
                        <form @submit.prevent="onProsesSuratPernyataan">
                            <div class="field">
                                <label class="label">Tugas</label>
                                <div class="control">
                                    <div class="select">
                                        <select title="Pilih jenis tugas">
                                            <option value="pendidikan">Pendidikan</option>
                                            <option value="kerekayasaan">Kerekayasaan</option>
                                            <option value="penunjang">Penunjang</option>
                                            <option value="profesi">Profesi</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div class="field">
                                <label class="label">Tanggal awal {{fields.tglAwal.valid}}</label>
                                <div class="control has-icons-right">
                                    <flat-pickr placeholder="Pilih tanggal"
                                                v-validate="'required'"
                                                v-model="tglAwal"
                                                name="tglAwal"
                                                class="input"
                                                :class="{'is-danger': errors.has('tglAwal')}"></flat-pickr>
                                    <span class="icon is-small is-right">
                                        <i class="fa fa-calendar"></i>
                                    </span>
                                </div>
                                <p class="help is-danger" v-show="errors.has('tglAwal')">Tidak boleh kosong</p>
                            </div>
                            <div class="field">
                                <label class="label">Tanggal akhir {{fields.tglAkhir.valid}}</label>
                                <div class="control has-icons-right">
                                    <flat-pickr placeholder="Pilih tanggal"
                                                v-validate="'required'"
                                                v-model="tglAkhir"
                                                name="tglAkhir"
                                                class="input"
                                                :class="{'is-danger': errors.has('tglAkhir')}"></flat-pickr>
                                    <span class="icon is-small is-right">
                                        <i class="fa fa-calendar"></i>
                                    </span>
                                </div>
                                <p class="help is-danger" v-show="errors.has('tglAkhir')">Tidak boleh kosong</p>
                            </div>
                            <button type="submit"
                                    class="button is-fullwidth is-primary is-radiusless"
                                    :disabled="!isButtonValid">
                                Proses
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div class="column">
            <div class="box">
                Auto
            </div>
        </div>
    </div>
</template>

<script>
    import flatPickr from 'vue-flatpickr-component';
    import 'flatpickr/dist/flatpickr.css';

    export default {
        data() {
            return {
                tglAwal: '',
                tglAkhir: '',
            }
        },
        components: {
            flatPickr
        },
        methods: {
            onProsesSuratPernyataan() {
                this.$validator.validateAll()
                    .then((res) => {
                        console.log(res);
                    })
                    .catch((err) => {
                        console.log(err);
                    });
            }
        },
        computed: {
            isButtonValid() {
                return this.fields.tglAwal.valid && this.fields.tglAkhir.valid;
            }
        }
    }
</script>