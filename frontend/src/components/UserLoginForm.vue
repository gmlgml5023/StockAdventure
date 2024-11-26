<template>
    <div class="login-container">
      <h1 class="login-title">Welcome to StockVenture</h1>
      <form @submit.prevent="logIn" class="login-form">
        <div class="form-group">
          <label for="username">ID</label>
          <input type="text" id="username" v-model.trim="username" required class="form-input" placeholder="Enter your username">
        </div>
  
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model.trim="password" required class="form-input" placeholder="Enter your password">
        </div>
  
        <button type="submit" class="login-button">
          <span class="button-text">추천 종목 보러 가기</span>
          <span class="star-icon">⭐</span>
        </button>
      </form>
    </div>
  </template>
  
  
<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const username = ref('')
const password = ref('')

const store = useAuthStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 30px;
  border-radius: 15px;
  background: rgba(0, 0, 0, 0.3);  /* 배경 투명도 증가 */
  backdrop-filter: blur(15px);      /* 블러 효과 강화 */
  border: 1px solid rgba(240, 219, 55, 0.2);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 0 32px rgba(240, 219, 55, 0.05);  /* 내부 그림자 추가 */
}

.login-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 28px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.form-group {
  margin-bottom: 20px;
}

label {
  color: #f0db37;
  margin-bottom: 8px;
  display: block;
  font-weight: 500;
  text-shadow: 0 0 8px rgba(240, 219, 55, 0.4);
}

.form-input {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background: rgba(0, 0, 0, 0.2);  /* 입력창 배경 투명도 증가 */
  color: #f0db37;
  font-size: 16px;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.form-input::placeholder {
  color: rgba(240, 219, 55, 0.4);
}

.form-input:focus {
  outline: none;
  border-color: #f0db37;
  box-shadow: 0 0 15px rgba(240, 219, 55, 0.2);
  background: rgba(0, 0, 0, 0.3);
}

.login-button {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: none;
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 0.9), 
    rgba(255, 209, 4, 0.9)
  );
  color: #000;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  backdrop-filter: blur(5px);
}

.login-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 1), 
    rgba(255, 209, 4, 1)
  );
}

.star-icon {
  font-size: 18px;
  text-shadow: 0 0 10px rgba(240, 219, 55, 0.6);
}
</style>