const tugas = {
    tanggal: null,
    jenis: null,
    butir: null,
    angka: 0.,
    satuan: null,
    uraian_singkat: null,
    taskPackages: []
};

const getTugasByName = (state) => (name) => {
    if (name) {
        return state.tugas[name];
    } else {
        return state.tugas;
    }
};

export {tugas, getTugasByName};
