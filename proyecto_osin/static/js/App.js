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
const app = new Vue({
    el: '#app',
    components: {
        example
    }
});