import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        tugas: 'Pendidikan'
    },
    getters: {
        jenisTugas(state) {
            return state.tugas;
        }
    },
    mutations: {
        setTugas(state, jenis) {
            state.tugas = jenis;
        }
    }
});