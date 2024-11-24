import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import ArticleView from "@/views/ArticleView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import ArticleCreateView from "@/views/ArticleCreateView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView,
    },
    {
      path: "/articles/",
      name: "ArticleView",
      component: ArticleView,
    },
    {
      path: "/articles/:article_id",
      name: "ArticleDetailView",
      component: ArticleDetailView,
    },
    {
      path: "/create",
      name: "ArticleCreateView",
      component: ArticleCreateView,
    },
  ],
});

export default router;
