import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleFormView from '../views/ArticleFormView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/articles',
    name: 'article-list',
    component: ArticleListView
  },
  {
    path: '/articles/:id',
    name: 'article-detail',
    component: ArticleDetailView
  },
  {
    path: '/articles/create',
    name: 'article-create',
    component: ArticleFormView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router