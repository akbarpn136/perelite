import Utama from './components/Utama.vue';

const Tugas = (resolve) => require(['./components/tugas/Tugas.vue'], resolve);
const TugasBaru = (resolve) => require(['./components/tugas/managed/ManageTugas.vue'], resolve);
const Profil = (resolve) => require(['./components/pengaturan/Profil.vue'], resolve);

export const routes = [
    {path: '/', component: Utama, name: 'utama', children: [
        {path: 'tugas', component: TugasBaru, name: 'tugasBaru'},
        {path: 'pendidikan', component: Tugas, name: 'pendidikan'},
        {path: 'kerekayasaan', component: Tugas, name: 'kerekayasaan'},
        {path: 'profesi', component: Tugas, name: 'profesi'},
        {path: 'penunjang', component: Tugas, name: 'penunjang'},
        {path: 'profil', component: Profil, name: 'profil'},
    ]},
    {path: '**', redirect: {name: 'utama'}},
];