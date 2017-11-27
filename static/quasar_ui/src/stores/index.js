import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        showModalTugas: false,
        taskPackages: [],
        ActiveTaskTab: {
            TabName: null,
            LkActive: false,
            LbActive: false,
            TnActive: false,
            OthersActive: false
        }
    },
    getters: {
        getShowModalTugas(state) {
            return state.showModalTugas;
        },
        getTaskPackages(state) {
            return state.taskPackages;
        },
        getActiveTaskTab(state) {
            return state.ActiveTaskTab;
        }
    },
    mutations: {
        setShowModalTugas(state, stats) {
            state.showModalTugas = stats;
        },
        setTaskPackages(state, payload) {
            state.taskPackages.push(payload);
        },
        clearTaskPackages(state) {
            state.taskPackages = [];
        },
        setActiveTaskTab(state, payload) {
            state.ActiveTaskTab.TabName = payload.TabName;
            state.ActiveTaskTab.LkActive = payload.LkActive;
            state.ActiveTaskTab.LbActive = payload.LbActive;
            state.ActiveTaskTab.TnActive = payload.TnActive;
            state.ActiveTaskTab.OthersActive = payload.OthersActive;
        }
    }
});
