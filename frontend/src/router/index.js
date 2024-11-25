import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";

// Stock
import StockView from '@/views/StockView.vue';

// Community
import ArticleView from "@/views/ArticleView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import ArticleCreateView from "@/views/ArticleCreateView.vue";

// Journal
import JournalView from "@/views/JournalView.vue";
import JournalDetailView from "@/views/JournalDetailView.vue";
import JournalCreateView from "@/views/JournalCreateView.vue";

// User Management
import SignupView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import InvestmentTestView from "@/views/InvestmentTestView.vue";
import InvestmentResultView from "@/views/InvestmentResultView.vue";
import UserProfileView from "@/views/UserProfileView.vue";
import UpdateProfileView from "@/views/UpdateProfileView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Home
    { path: "/", name: "home", component: HomeView },

    // Stock
    { path: '/stocklist/', name: 'StockView', component: StockView },

    // Community
    { path: "/articles/", name: "ArticleView", component: ArticleView },
    { path: "/articles/:article_id/", name: "ArticleDetailView", component: ArticleDetailView },
    { path: "/create", name: "ArticleCreateView", component: ArticleCreateView },
    
    // Journal
    { path: "/journals/", name: "JournalView", component: JournalView },
    { path: "/journals/:journal_id/", name: "JournalDetailView", component: JournalDetailView },
    { path: "/journals/create", name: "JournalCreateView", component: JournalCreateView },

    // User Management & Test
    { path: "/signup/", name: "signup", component: SignupView },
    { path: "/login/", name: "login", component: LogInView },
    { path: "/investment_style/test/", name: "investment-test", component: InvestmentTestView },
    { path: "/investment_style/result/", name: "investment-result", component: InvestmentResultView },
    { path: "/accounts/:username/", name: "user-profile", component: UserProfileView, props: true },
    { path: "/accounts/:username/update/", name: "update-profile", component: UpdateProfileView, props: true },

  ],
});

export default router;
