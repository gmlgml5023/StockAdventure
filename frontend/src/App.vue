<template>
  <div id="app">
    <h1>StockAdventure</h1>
    <nav>
       <template v-if="store.isLogin">
        <button @click="logOut" class="nav-button">로그아웃</button>
        <router-link to="/investment_style/test" class="nav-button"
          >투자 성향 테스트</router-link
        >
        <router-link to="/account/:username" class="nav-button"
          >유저 프로필</router-link
        >
        <RouterLink to="/stocklist/">주식정보조회</RouterLink> |
        <RouterLink to="/journals/">매매일지</RouterLink> |
        <RouterLink to="/articles/">커뮤니티</RouterLink>
      </template>
      <template v-else>
        <router-link to="/signup" class="nav-button">회원가입</router-link> ㅣ
        <router-link to="/login" class="nav-button">로그인</router-link>
      </template>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const store = useAuthStore();

const logOut = function () {
  store.logOut();
};
</script>

<style scoped>
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  margin-bottom: 30px;
  padding: 20px 0;
  border-bottom: 1px solid #eee;
}

h1 {
  color: #333;
  font-size: 24px;
  font-weight: bold;
}

main {
  min-height: calc(100vh - 150px);
}

</style>
=======
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
  transition: background-color 0.3s;
  border: none;
  cursor: pointer;
}

.nav-button:hover {
  background-color: #ddd;
}
</style>