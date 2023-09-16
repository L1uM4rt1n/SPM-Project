import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router/router'
import '@fortawesome/fontawesome-free/js/all'
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)

// Use FontAwesome
app.config.globalProperties.$fontawesome = require('@fortawesome/fontawesome-svg-core')

// Use BootstrapVue
app.use(router)
app.use(BootstrapVue3)

app.mount('#app')
