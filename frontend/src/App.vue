<template>
  <div>
    <nav>
      <router-link to="/signup" class="nav-button">회원가입</router-link>
      <router-link to="/login" class="nav-button">로그인</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup>
</script>

<style scoped>
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
}

.nav-button:hover {
  background-color: #ddd;
}
</style>