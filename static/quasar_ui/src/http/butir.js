import axios from 'axios';

const URL = process.env.NODE_ENV === 'development' ? 'http://localhost:8000/' : 'http://bbta3.bppt.go.id:9601/';

const QWERTY = JSON.parse(localStorage.getItem('qwerty')) ||
    JSON.parse({uid: ''});

function GetButir(kategori=null) {
    return axios.get(`${URL}utility/api1/butir/${kategori}/`, {
        headers: {
            'Authorization': `Bearer ${QWERTY.uid}`,
            'Content-Type': 'application/json'
        }
    });
}

export {GetButir};
