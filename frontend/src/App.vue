<template>
  <div id="app">
    <router-view></router-view>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/journals/">매매일지</RouterLink>
  </nav>
  <h1>Stock Adventure</h1>
  <RouterView />
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>
