import Utama from './components/Utama.vue';

const Pendidikan = (resolve) => require(['./components/tugas/Pendidikan.vue'], resolve);
const PendidikanTambah = (resolve) => require(['./components/tugas/managed/ManagePendidikan.vue'], resolve);

const Kerekayasaan = (resolve) => require(['./components/tugas/Kerekayasaan.vue'], resolve);
const KerekayasaanTambah = (resolve) => require(['./components/tugas/managed/ManageKerekayasaan.vue'], resolve);

const Profesi = (resolve) => require(['./components/tugas/Profesi.vue'], resolve);
const ProfesiTambah = (resolve) => require(['./components/tugas/managed/ManageProfesi.vue'], resolve);

const Penunjang = (resolve) => require(['./components/tugas/Penunjang.vue'], resolve);
const PenunjangTambah = (resolve) => require(['./components/tugas/managed/ManagePenunjang.vue'], resolve);

const Profil = (resolve) => require(['./components/pengaturan/Profil.vue'], resolve);

export const routes = [
    {path: '/', component: Utama, name: 'utama'},
    {path: '/pendidikan', component: Pendidikan, name: 'pendidikan', children: [
        {path: 'tambah', component: PendidikanTambah, name: 'pendidikanBaru'}
    ]},
    {path: '/kerekayasaan', component: Kerekayasaan, name: 'kerekayasaan', children: [
        {path: 'tambah', component: KerekayasaanTambah, name: 'kerekayasaanBaru'}
    ]},
    {path: '/profesi', component: Profesi, name: 'profesi', children: [
        {path: 'tambah', component: ProfesiTambah, name: 'profesiBaru'}
    ]},
    {path: '/penunjang', component: Penunjang, name: 'penunjang', children: [
        {path: 'tambah', component: PenunjangTambah, name: 'penunjangBaru'}
    ]},
    {path: '/profil', component: Profil, name: 'profil'},
    {path: '**', redirect: {name: 'utama'}},
];