import Vue from 'vue';
import App from './App.vue';
import Router from 'vue-router';
import VeeValidate, {Validator} from 'vee-validate';
import id from 'vee-validate/dist/locale/id';
import {routes} from './routes';
import store from './stores';

Vue.use(Router);

Validator.localize('id', id);
Vue.use(VeeValidate, {
  locale: 'id'
});

const router = new Router({
    routes
});

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});
