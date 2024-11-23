import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import JournalView from '@/views/JournalView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'

const routes = [
  {path: '/', name: 'HomeView', component: HomeView},
  {path: '/journals/', name: 'JournalView', component: JournalView},
  {path: '/journals/:journal_id', name: 'DetailView', component: DetailView},
  {path: '/journals/create', name: 'CreateView', component: CreateView}
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router