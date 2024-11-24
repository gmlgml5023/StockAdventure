import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import JournalView from "@/views/JournalView.vue";
import JournalDetailView from "@/views/JournalDetailView.vue";
import JournalCreateView from "@/views/JournalCreateView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView,
    },
    {
      path: "/journals/",
      name: "JournalView",
      component: JournalView,
    },
    {
      path: "/journals/:journal_id",
      name: "JournalDetailView",
      component: JournalDetailView,
    },
    {
      path: "/journals/create",
      name: "JournalCreateView",
      component: JournalCreateView,
    },
  ],
});

export default router;
