import axios from 'axios';

const URL = process.env.NODE_ENV === 'development' ?
    'http://localhost:8000/' :
    'http://bbta3.bppt.go.id:9601/';

const QWERTY = JSON.parse(localStorage.getItem('qwerty')) || null;

function TambahTugas(payload) {
    return axios.post(`${URL}core/api1/tugas/`, payload, {
        headers: {
            'Authorization': `Bearer ${QWERTY.uid}`
        }
    });
}

export {TambahTugas};
