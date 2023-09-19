import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router/router'
import '@fortawesome/fontawesome-free/js/all'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App)

// Use FontAwesome
app.config.globalProperties.$fontawesome = require('@fortawesome/fontawesome-svg-core')

// Use BootstrapVue
app.use(router)

app.mount('#app')
