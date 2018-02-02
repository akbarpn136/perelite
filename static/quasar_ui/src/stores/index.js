import Vue from 'vue'
import Vuex from 'vuex';
import * as _ from 'lodash';
import {lk, getLkByName} from './tugas/lk';
import {lb, getLbByName} from './tugas/lb';
import {tugas, tugasRinci, getTugasByName} from './tugas/tugas';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        ActiveTaskTab: {
            TabName: null,
            LkActive: false,
            LbActive: false,
            TnActive: false,
            OthersActive: false
        },
        tugas,
        tugasRinci,
        lk,
        lb
    },
    getters: {
        getActiveTaskTab(state) {
            return state.ActiveTaskTab;
        },
        getTaskPackages(state) {
            return state.tugas.taskPackages;
        },
        getTugasRinci(state) {
            return state.tugasRinci;
        },
        getTugasByName,
        getLkByName,
        getLbByName
    },
    mutations: {
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
            _.forEach(state.ActiveTaskTab, (v, k) => {
                state.ActiveTaskTab[k] = payload[k];
            });
        },
        setTugasRinci(state, payload) {
            _.forEach(payload, (v, k) => {
                state.tugasRinci[k] = payload[k];
            });
        },
        setTugas(state, payload) {
            state.tugas[payload.nama] = payload.value;
        },
        setLk(state, payload) {
            state.lk[payload.nama] = payload.value;
        },
        setLb(state, payload) {
            state.lb[payload.nama] = payload.value;
        }
    }
});
