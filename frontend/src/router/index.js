import { createRouter, createWebHistory } from "vue-router";
import SignupView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import HomeView from "@/views/HomeView.vue";
import InvestmentTestView from "@/views/InvestmentTestView.vue";
import InvestmentResultView from "@/views/InvestmentResultView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/login",
      name: "login",
      component: LogInView,
    },
    {
      path: "/investment_style/test/",
      name: "investment-test",
      component: InvestmentTestView,
    },
    {
      path: "/investment_style/result/",
      name: "investment-result",
      component: InvestmentResultView,
    },
  ],
});

export default router;
