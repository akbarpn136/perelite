import Vue from 'vue';
import App from './App.vue';
import Router from 'vue-router';
import VeeValidate from 'vee-validate';
import {routes} from './routes';

Vue.use(Router);
Vue.use(VeeValidate);

const router = new Router({
    routes
});

new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
