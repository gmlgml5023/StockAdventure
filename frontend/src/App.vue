<template>
  <div id="app" class="app">
    <div class="nav-container">
      <a href="http://localhost:5173/" class="logo-link">
        <h1 class="logo">StockAdventure</h1>
      </a>
      <nav v-if="authStore.isLogin" class="nav-menu">
        <RouterLink to="/" class="nav-button">주식정보조회</RouterLink>
        <RouterLink to="/stocks/recommendations/" class="nav-button">추천종목조회</RouterLink>
        <RouterLink to="/journals/" class="nav-button">매매일지</RouterLink>
        <RouterLink to="/articles/" class="nav-button">커뮤니티</RouterLink>
        <RouterLink to="/investment_style/test" class="nav-button">투자 성향 테스트</RouterLink>
        <RouterLink 
          v-if="authStore.username" 
          :to="{ name: 'user-profile', params: { username: authStore.username } }" 
          class="nav-button"
        >마이페이지</RouterLink>
        <button @click="logOut" class="nav-button logout-button">로그아웃</button>
      </nav>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

const logOut = () => {
  authStore.logOut();
};
</script>

<style scoped>
.app {
  min-height: 100vh;
  background: url('@/assets/space-background.jpg') no-repeat center center fixed;
  background-size: cover;
}

.nav-container {
  margin: 0 auto;
  padding: 20px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(240, 219, 55, 0.2);
}

.logo-link {
  text-decoration: none;
}

.logo {
  color: #f0db37;
  font-size: 32px;
  font-weight: bold;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 20px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.nav-menu {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 15px;
  padding: 10px 0;
}

.nav-button {
  padding: 10px 20px;
  text-decoration: none;
  color: #f0db37;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(240, 219, 55, 0.4);
  border-radius: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
  backdrop-filter: blur(5px);
}

.nav-button:hover {
  transform: translateY(-2px);
  background: rgba(240, 219, 55, 0.2);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.2);
}

.nav-button.router-link-active {
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 0.9), 
    rgba(255, 209, 4, 0.9)
  );
  color: #000;
  border: none;
}

.logout-button {
  background: rgba(255, 71, 87, 0.2);
  border-color: rgba(255, 71, 87, 0.4);
  color: #ff4757;
}

.logout-button:hover {
  background: rgba(255, 71, 87, 0.3);
  box-shadow: 0 5px 15px rgba(255, 71, 87, 0.2);
}

@media (max-width: 768px) {
  .nav-menu {
    flex-direction: column;
    align-items: center;
  }

  .nav-button {
    width: 100%;
    text-align: center;
  }
}
</style>