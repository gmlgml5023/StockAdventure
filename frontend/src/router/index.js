// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import StockList from '../views/StockList.vue'  // 경로 주의

const routes = [
  {
    path: '/',
    name: 'StockList',
    component: StockList
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router