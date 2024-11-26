import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import HomeView from "@/views/HomeView.vue";
import IntroView from "@/views/IntroView.vue";

// Stocks
import StockRecommendationView from "@/views/StockRecommendationView.vue";

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
import UserProfileUpdateView from "@/views/UserProfileUpdateView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", name: "home", component: HomeView, meta: { requiresAuth: true } },
    { path: "/intro", name: "intro", component: IntroView },

    // Stocks
    { path: "/stocks/recommendations/", name: "StockRecommendationView", component: StockRecommendationView, meta: { requiresAuth: true } },

    // Community
    { path: "/articles/", name: "ArticleView", component: ArticleView, meta: { requiresAuth: true } },
    { path: "/articles/:article_id/", name: "ArticleDetailView", component: ArticleDetailView, meta: { requiresAuth: true } },
    { path: "/create", name: "ArticleCreateView", component: ArticleCreateView, meta: { requiresAuth: true } },
    
    // Journal
    { path: "/journals/", name: "JournalView", component: JournalView, meta: { requiresAuth: true } },
    { path: "/journals/:journal_id/", name: "JournalDetailView", component: JournalDetailView, meta: { requiresAuth: true } },
    { path: "/journals/create", name: "JournalCreateView", component: JournalCreateView, meta: { requiresAuth: true } },
    { path: "/:username/journals/", name: "user-journal", component: JournalView, meta: { requiresAuth: true } },


    // User Management & Test
    { path: "/signup/", name: "signup", component: SignupView },
    { path: "/login/", name: "login", component: LogInView },
    { path: "/investment_style/test/", name: "investment-test", component: InvestmentTestView, meta: { requiresAuth: true } },
    { path: "/investment_style/result/", name: "investment-result", component: InvestmentResultView, meta: { requiresAuth: true } },
    { path: "/accounts/:username/", name: "user-profile", component: UserProfileView, props: true, meta: { requiresAuth: true } },
    { path: "/accounts/:username/update/", name: "update-profile", component: UserProfileUpdateView, props: true, meta: { requiresAuth: true } },
  ]
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const isAuthenticated = authStore.isLogin;

  if (to.meta.requiresAuth && !isAuthenticated) {
    if (to.path === '/') {
      next({ name: 'intro' });
    } else {
      next({ name: 'login', query: { redirect: to.fullPath } });
    }
  } else if ((to.name === 'login' || to.name === 'signup') && isAuthenticated) {
    next({ name: 'home' });
  } else if (to.name === 'intro' && isAuthenticated) {
    next({ name: 'home' }); // 로그인 상태에서 intro 페이지 접근 시 홈으로 리다이렉트
  } else {
    next();
  }
});
export default router;