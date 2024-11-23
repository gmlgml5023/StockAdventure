import { createRouter, createWebHistory } from "vue-router";
import SignupView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import HomeView from "@/views/HomeView.vue";
import InvestmentTestView from "@/views/InvestmentTestView.vue";
import InvestmentResultView from "@/views/InvestmentResultView.vue";
import UserProfileView from "@/views/UserProfileView.vue";
import UpdateProfileView from "@/views/UpdateProfileView.vue";

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
      path: "/investment_style/test",
      name: "investment-test",
      component: InvestmentTestView,
    },
    {
      path: "/investment_style/result",
      name: "investment-result",
      component: InvestmentResultView,
    },
    {
      path: "/accounts/:username",
      name: "user-profile",
      component: UserProfileView,
      props: true,
    },
    {
      path: "/accounts/:username/update",
      name: "update-profile",
      component: UpdateProfileView,
      props: true,
    },
  ],
});

export default router;
