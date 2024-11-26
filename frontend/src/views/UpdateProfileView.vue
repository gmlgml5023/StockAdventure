<template>
  <div>
    <UserUpdateProfileForm :username="username" />
  </div>
</template>

<script setup>
import UserUpdateProfileForm from '@/components/UserUpdateProfileForm.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const username = route.params.username
</script>