// State
const lb = {
    nama: 'LOGBOOK',
    nomor: null,
    kode_peran: null,
    judul: null,
    unit_kerja: null,
    pusat_kerja: null,
    uraian_lengkap: null,
    nama_pemberi: null,
    peran_pemberi: null,
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
