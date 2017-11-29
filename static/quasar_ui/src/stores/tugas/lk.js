// State
const lk = {
    nama: 'LEMBAR KERJA',
    kode_peran: null,
    nomor: null,
    referensi: null,
    program: null,
    wbs_wp: null,
    uraian_lengkap: null,
    nama_pemberi: null,
    peran_pemberi: null,
    validasi: null
};


// Getters
const getLkByName = (state) => (name) => {
    if (name) {
        return state.lk[name];
    } else {
        return state.lk;
    }
};

export {lk, getLkByName};
