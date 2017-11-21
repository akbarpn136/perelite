import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        showModalTugas: false
    },
    getters: {
        getShowModalTugas(state) {
            return state.showModalTugas;
        }
    },
    mutations: {
        setShowModalTugas(state, stats) {
            state.showModalTugas = stats;
        }
    }
});
