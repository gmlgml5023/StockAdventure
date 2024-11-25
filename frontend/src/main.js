import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)


// app.config.globalProperties.$axios = axios.create({
//     baseURL: 'http://127.0.0.1:8000/',
// })


app.use(router)
app.use(pinia)

app.mount('#app')

