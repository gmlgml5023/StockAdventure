<template>
  <div id="app" class="app">
    <a href="http://localhost:5173/"><h1>StockAdventure</h1></a>
    <nav v-if="store.isLogin">
      <RouterLink to="/" class="nav-button">주식정보조회</RouterLink>
      <RouterLink to="/journals/" class="nav-button">매매일지</RouterLink>
      <RouterLink to="/articles/" class="nav-button">커뮤니티</RouterLink>
      <RouterLink to="/investment_style/test" class="nav-button">투자 성향 테스트</RouterLink>
      <RouterLink v-if="store.username" :to="{ name: 'user-profile', params: { username: store.username } }" class="nav-button">유저 프로필</RouterLink>
      <button @click="logOut" class="nav-button">로그아웃</button>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();

const logOut = () => {
  store.logOut();
};
</script>

<style scoped>
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
  font-size: 24px;
  font-weight: bold;
}

nav {
  padding: 20px;
  text-align: center;
}

.nav-button {
  display: inline-block;
  margin: 0 10px;
  padding: 10px 20px;
  text-decoration: none;
  color: #333;
  background-color: #f0f0f0;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-button:hover {
  background-color: #ddd;
}
</style>