import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    }
  ]
})

export default router