<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <label for="username">사용자명: </label>
      <input type="text" id="username" v-model.trim="username" /><br />

      <label for="email">이메일: </label>
      <input type="email" id="email" v-model.trim="email" /><br />

      <label for="nickname">닉네임: </label>
      <input type="text" id="nickname" v-model.trim="nickname" /><br />

      <label for="password1">비밀번호: </label>
      <input type="password" id="password1" v-model.trim="password1" /><br />

      <label for="password2">비밀번호 확인: </label>
      <input type="password" id="password2" v-model.trim="password2" />

      <input type="submit" value="가입하기" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";

const username = ref(null);
const email = ref(null);
const nickname = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const store = useAuthStore();

const signUp = async function () {
  try {
    const payload = {
      username: username.value,
      email: email.value,
      nickname: nickname.value,
      password1: password1.value,
      password2: password2.value,
    };
    await store.signUp(payload);
    // 성공 시 처리 (예: 로그인 페이지로 이동)
  } catch (error) {
    // 에러 처리
    console.error("회원가입 처리 중 오류:", error);
  }
};
</script>
