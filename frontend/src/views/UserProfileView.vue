<template>
  <div class="profile-view">
    <UserProfile :username="username" />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import UserProfile from '@/components/UserProfile.vue'

const route = useRoute()
const username = route.params.username
</script>

<style scoped>
.profile-view {
  min-height: 100vh;
  padding: 20px;
  background: url('@/assets/space-background.jpg') no-repeat center center fixed;
  background-size: cover;
}
</style>