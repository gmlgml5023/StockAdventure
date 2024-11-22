<!-- src/App.vue -->
<template>
  <div class="app">
    <header>
      <h1>Stock Adventure</h1>
    </header>
    
    <main>
      <router-view></router-view>
    </main>
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
</style>