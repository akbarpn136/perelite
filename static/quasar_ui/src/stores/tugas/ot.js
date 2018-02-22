// State
const ot = {
    nama: 'OTHERS',
    url: null,
    nomor: null,
    validasi: null
};


// Getters
const getOtByName = (state) => (name) => {
    if (name) {
        return state.ot[name];
    } else {
        return state.ot;
    }
};

export {ot, getOtByName};
