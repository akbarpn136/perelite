import axios from 'axios';

const URL = process.env.NODE_ENV === 'development' ?
    'http://localhost:8000/' :
    'http://bbta3.bppt.go.id:9601/';

const QWERTY = JSON.parse(localStorage.getItem('qwerty')) ||
    JSON.parse({uid: ''});
const URL_TUGAS = `${URL}core/api1/tugas/`;

function LihatTugas(kategori=null, tglAwal=null, tglAkhir=null, page=1) {
    return axios.get(`${URL_TUGAS}${kategori}/`, {
        headers: {
            'Authorization': `Bearer ${QWERTY.uid}`
        },
        params: {
            tglAwal,
            tglAkhir,
            page,
        }
    });
}

function TambahTugas(payload) {
    return axios.post(URL_TUGAS, payload, {
        headers: {
            'Authorization': `Bearer ${QWERTY.uid}`
        }
    });
}

export {LihatTugas, TambahTugas};
