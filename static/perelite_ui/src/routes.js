import Utama from './components/Utama.vue';

const Pendidikan = (resolve) => require(['./components/tugas/Pendidikan.vue'], resolve);
const Kerekayasaan = (resolve) => require(['./components/tugas/Kerekayasaan.vue'], resolve);
const Profesi = (resolve) => require(['./components/tugas/Profesi.vue'], resolve);
const Penunjang = (resolve) => require(['./components/tugas/Penunjang.vue'], resolve);
const Profil = (resolve) => require(['./components/pengaturan/Profil.vue'], resolve);

export const routes = [
    {path: '/', component: Utama, name: 'utama'},
    {path: '/pendidikan', component: Pendidikan, name: 'pendidikan'},
    {path: '/kerekayasaan', component: Kerekayasaan, name: 'kerekayasaan'},
    {path: '/profesi', component: Profesi, name: 'profesi'},
    {path: '/penunjang', component: Penunjang, name: 'penunjang'},
    {path: '/profil', component: Profil, name: 'profil'},
    {path: '**', redirect: {name: 'utama'}},
];