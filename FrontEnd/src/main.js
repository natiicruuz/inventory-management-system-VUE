import { createApp } from 'vue';
import App from './App.vue';
import { provideApollo } from './apollo.js';
import { router } from './router'
import './style.css'; 

const app = createApp(App);
app.use(router);
provideApollo(app);
app.mount('#app');

