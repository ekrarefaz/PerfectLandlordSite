import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

// axios.defaults.baseURL = 'https://203.16.241.202/api/';
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';

createApp(App).use(store).use(router, axios).mount('#app');
