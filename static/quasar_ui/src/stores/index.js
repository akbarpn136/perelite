import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        showModalTugas: false,
        taskPackages: []
    },
    getters: {
        getShowModalTugas(state) {
            return state.showModalTugas;
        },
        getTaskPackages(state) {
            return state.taskPackages;
        }
    },
    mutations: {
        setShowModalTugas(state, stats) {
            state.showModalTugas = stats;
        },
        setTaskPackages(state, payload) {
            state.taskPackages.push(payload);
        }
    }
});
