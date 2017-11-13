import Vue from 'vue';
import App from './App.vue';
import Router from 'vue-router';
import {routes} from './routes';

Vue.use(Router);

const router = new Router({
    routes
});

new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
