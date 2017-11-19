<template>
    <div class="card">
        <header class="card-header">
            <div class="card-header-title">
                Form Tugas
            </div>
            <div class="card-header-icon" aria-label="more options">
                <span class="icon">
                    <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                </span>
            </div>
        </header>
        <div class="card-content">
            <form @submit.prevent="onTugasSubmit('formTugas')"
                  data-vv-scope="formTugas">
                <div class="columns">
                    <div class="column">
                        <div class="field">
                            <label class="label">Tanggal</label>
                            <div class="control has-icons-right">
                                <flat-pickr placeholder="Pilih tanggal"
                                            v-validate="'required'"
                                            v-model="tanggal"
                                            name="tanggal"
                                            class="input"
                                            :class="{'is-danger': errors.has('formTugas.tanggal')}"></flat-pickr>
                                <span class="icon is-small is-right">
                                    <i class="fa fa-calendar"></i>
                                </span>
                            </div>
                            <p class="help is-danger" v-show="errors.has('formTugas.tanggal')">
                                {{errors.first('formTugas.tanggal')}}
                            </p>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field">
                            <label class="label" for="kategori">Jenis</label>
                            <div class="control is-expanded">
                                <div class="select is-fullwidth">
                                    <select id="kategori"
                                            name="jenis"
                                            v-model="jenis"
                                            v-validate="'required'">
                                        <option value="pendidikan">Pendidikan</option>
                                        <option value="kerekayasaan">Kerekayasaan</option>
                                        <option value="profesi">Profesi</option>
                                        <option value="penunjang">Penunjang</option>
                                    </select>
                                </div>
                            </div>
                            <p class="help is-danger" v-show="errors.has('formTugas.jenis')">
                                {{errors.first('formTugas.jenis')}}
                            </p>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field">
                            <label class="label">Butir</label>
                            <div class="control">
                                <input class="input"
                                       type="text"
                                       placeholder="Butir kegiatan"
                                       name="butir"
                                       v-validate="'required'"
                                       v-model="butir">
                            </div>
                            <p class="help"
                               :class="{'is-danger': errors.has('formTugas.butir')}">{{errors.first('formTugas.butir')}}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="columns">
                    <div class="column">
                        <div class="field">
                            <label class="label">Angka Kredit</label>
                            <div class="control">
                                <input class="input"
                                       type="text"
                                       placeholder="Angka kegiatan yang diperoleh"
                                       name="angka"
                                       v-model="angka"
                                       v-validate="'required|decimal'" readonly>
                            </div>
                            <p class="help"
                               :class="{'is-danger': errors.has('formTugas.angka')}">{{errors.first('formTugas.angka')}}</p>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field">
                            <label class="label">Satuan Hasil</label>
                            <div class="control">
                                <input class="input"
                                       type="text"
                                       placeholder="Butir kegiatan"
                                       name="satuan"
                                       v-model="satuan"
                                       v-validate="'required'" readonly>
                            </div>
                            <p class="help"
                               :class="{'is-danger': errors.has('formTugas.satuan')}">{{errors.first('formTugas.satuan')}}
                            </p>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="columns">
                    <div class="column">
                        <div class="field">
                            <label class="label">Uraian Singkat Kegiatan</label>
                            <div class="control">
                            <textarea class="textarea"
                                      :class="{'is-danger': errors.has('formTugas.uraian_singkat')}"
                                      placeholder="Berikan uraian singkat disini"
                                      name="uraian_singkat"
                                      rows="2"
                                      v-validate="'required'"
                                      v-model="uraian_singkat"></textarea>
                            </div>
                            <p class="help"
                               :class="{'is-danger': errors.has('formTugas.uraian_singkat')}">{{errors.first('formTugas.uraian_singkat')}}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="columns">
                    <div class="column">
                        <div class="field">
                            <label class="label">Uraian Lengkap Kegiatan</label>
                            <div class="control">
                            <textarea class="textarea"
                                      placeholder="Berikan uraian lengkap disini"
                                      name="uraian_lengkap" rows="20"></textarea>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="field is-grouped">
                    <div class="control">
                        <button type="submit" class="button is-link">Simpan</button>
                    </div>
                    <div class="control">
                        <button type="button" class="button is-text">Batal</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import flatPickr from 'vue-flatpickr-component';
    import 'flatpickr/dist/flatpickr.css';
    import 'flatpickr/dist/themes/material_green.css';

    export default {
        data() {
            return {
                tanggal: '',
                jenis: '',
                butir: '',
                angka: null,
                satuan: '',
                uraian_singkat: '',
                uraian_lengkap: ''
            }
        },
        created() {
            this.$store.commit('setShowParent', false);
        },
        components: {
            flatPickr
        },
        methods: {
            onTugasSubmit(scope) {
                this.$validator.validateAll(scope).then((result) => {
                    if (result) {
                        console.log(result);
                    }
                });
            }
        }
    }
</script>