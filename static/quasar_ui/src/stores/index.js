import Vue from 'vue'
import Vuex from 'vuex';
import * as _ from 'lodash';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        showModalTugas: false,
        ActiveTaskTab: {
            TabName: null,
            LkActive: false,
            LbActive: false,
            TnActive: false,
            OthersActive: false
        },
        tugas: {
            tanggal: null,
            jenis: null,
            butir: null,
            angka: 0.,
            satuan: null,
            uraian_singkat: null,
            taskPackages: []
        },
        lk: {
            nama: 'LEMBAR KERJA',
            kode_peran: null,
            nomor: null,
            referensi: null,
            program: null,
            wbs_wp: null,
            uraian_lengkap: null,
            nama_pemberi: null,
            peran_pemberi: null
        }
    },
    getters: {
        getShowModalTugas(state) {
            return state.showModalTugas;
        },
        getActiveTaskTab(state) {
            return state.ActiveTaskTab;
        },
        getTugasByName: (state) => (name) => {
            if (name) {
                return state.tugas[name];
            } else {
                return state.tugas;
            }
        },
        getTaskPackages(state) {
            return state.tugas.taskPackages;
        },
        getLkByName: (state) => (name) => {
            if (name) {
                return state.lk[name];
            } else {
                return state.lk;
            }
        }
    },
    mutations: {
        setShowModalTugas(state, stats) {
            state.showModalTugas = stats;
        },
        setTaskPackages(state, key, payload) {
            let match = _.find(state.tugas.taskPackages, key);

            if (match) {
                let index = _.indexOf(state.tugas.taskPackages, match);
                state.tugas.taskPackages.splice(index, 1, payload);
            } else {
                state.tugas.taskPackages.push(payload);
            }
        },
        clearTaskPackages(state) {
            state.tugas.taskPackages = [];
        },
        setActiveTaskTab(state, payload) {
            state.ActiveTaskTab.TabName = payload.TabName;
            state.ActiveTaskTab.LkActive = payload.LkActive;
            state.ActiveTaskTab.LbActive = payload.LbActive;
            state.ActiveTaskTab.TnActive = payload.TnActive;
            state.ActiveTaskTab.OthersActive = payload.OthersActive;
        },
        setTugas(state, payload) {
            state.tugas[payload.nama] = payload.value;
        },
        setLk(state, payload) {
            state.lk[payload.nama] = payload.value;
        }
    }
});
