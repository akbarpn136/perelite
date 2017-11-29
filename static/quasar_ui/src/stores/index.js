import Vue from 'vue'
import Vuex from 'vuex';
import * as _ from 'lodash';
import {lk, getLkByName} from './tugas/lk';
import {tugas, getTugasByName} from './tugas/tugas';

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
        tugas,
        lk
    },
    getters: {
        getShowModalTugas(state) {
            return state.showModalTugas;
        },
        getActiveTaskTab(state) {
            return state.ActiveTaskTab;
        },
        getTaskPackages(state) {
            return state.tugas.taskPackages;
        },
        getTugasByName,
        getLkByName
    },
    mutations: {
        setShowModalTugas(state, stats) {
            state.showModalTugas = stats;
        },
        setTaskPackages(state, data) {
            let match = _.find(state.tugas.taskPackages, data.key);

            if (match) {
                let index = _.indexOf(state.tugas.taskPackages, match);
                state.tugas.taskPackages.splice(index, 1, data.payload);
            } else {
                state.tugas.taskPackages.push(data.payload);
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
