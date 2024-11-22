<template>
    <div>
      <h1>Sign Up Page</h1>
      <form @submit.prevent="signUp">
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username"><br>
  
        <label for="password1">password : </label>
        <input type="password" id="password1" v-model.trim="password1"><br>
  
        <label for="password2">password confirmation : </label>
        <input type="password" id="password2" v-model.trim="password2">
        
        <input type="submit" value="SignUp">
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useAuthStore } from '@/stores/auth'
  
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  
  const store = useAuthStore()
  
  const signUp = async function () {
    try {
      const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value
      }
      await store.signUp(payload)
      // 성공 시 처리 (예: 로그인 페이지로 이동)
    } catch (error) {
      // 에러 처리
      console.error('회원가입 처리 중 오류:', error)
    }
  }
  
  </script>
  
  <style>
  
  </style>