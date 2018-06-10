window._ = require('lodash');
//JQUERY
try {
    window.$ = window.jQuery = require('jquery')
    require('bootstrap-sass');
} catch (e) {}


window.axios = require('axios');
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

let token = document.querySelector('input[name="csrfmiddlewaretoken"]');
if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.value;
} else {
    console.error('CSRF token not found');
}

import Vue from 'vue';
import example from './components/Example.vue';
import persona from './components/Persona.vue';
import twiter from './components/Twitter.vue';
import github from './components/Github.vue';
import instagram from './components/Instagram.vue';
import clave from './components/Clave.vue';
const app = new Vue({
    el: '#app',
    components: {
        example,
        persona,
        twiter,
        github,
        instagram,
        clave
    }
});