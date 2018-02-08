// State
const tn = {
    nama: 'TECHNICAL NOTE',
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
const getTnByName = (state) => (name) => {
    if (name) {
        return state.tn[name];
    } else {
        return state.tn;
    }
};

export {tn, getTnByName};
