// State
const lb = {
    nama: 'LOGBOOK',
    nomor: null,
    kode_peran: null,
    judul: null,
    unit_kerja: null,
    pusat_kerja: null,
    uraian_lengkap: null,
    nama_pemeriksa: null,
    peran_pemeriksa: null,
    nama_penyetuju: null,
    peran_penyetuju: null,
    validasi: null
};


// Getters
const getLbByName = (state) => (name) => {
    if (name) {
        return state.lb[name];
    } else {
        return state.lb;
    }
};

export {lb, getLbByName};
