import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        tugas: 'Pendidikan',
        showParent: ''
    },
    getters: {
        jenisTugas(state) {
            return state.tugas;
        },
        getShowParent(state) {
            return state.showParent;
        }
    },
    mutations: {
        setTugas(state, jenis) {
            state.tugas = jenis;
        },
        setShowParent(state, value) {
            state.showParent = value;
        }
    }
});