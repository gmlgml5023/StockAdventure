import { createRouter, createWebHistory } from "vue-router"
import HomeView from "@/views/HomeView.vue"

// Stock
import StockList from '@/views/StockList.vue'

// Community
import ArticleView from "@/views/ArticleView.vue"
import ArticleDetailView from "@/views/ArticleDetailView.vue"
import ArticleCreateView from "@/views/ArticleCreateView.vue"

// Journal
import JournalView from "@/views/JournalView.vue"
import JournalDetailView from "@/views/JournalDetailView.vue"
import JournalCreateView from "@/views/JournalCreateView.vue"

///////////////////////////////////////////////////////////////////////////

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // stock
    { path: '/stocklist/', name: 'StockList', component: StockList }
    
    // Community
    { path: "/articles/", name: "ArticleView", component: ArticleView },
    { path: "/articles/:article_id", name: "ArticleDetailView", component: ArticleDetailView },
    { path: "/create", name: "ArticleCreateView", component: ArticleCreateView },
    
    // Journal
    { path: "/journals/", name: "JournalView", component: JournalView },
    { path: "/journals/:journal_id", name: "JournalDetailView", component: JournalDetailView },
    { path: "/journals/create", name: "JournalCreateView", component: JournalCreateView },
  ]
})

export default router
