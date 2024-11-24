<template>
  <div id="app">
    <nav>
      <RouterLink to="/stocklist/">주식정보조회</RouterLink> |
      <RouterLink to="/journals/">매매일지</RouterLink> |
      <RouterLink to="/articles/">커뮤니티</RouterLink>
    </nav>
    <router-view/>
  </div>
</template>

<script setup>
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
