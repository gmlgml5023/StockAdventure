<template>
    <div class="signup-container">
      <h1 class="signup-title">Welcome to StockVenture</h1>
      <form @submit.prevent="signUp" class="signup-form">
        <div class="form-group">
          <label for="username">ID</label>
          <input 
            type="text" 
            id="username" 
            v-model.trim="username" 
            required 
            class="form-input"
            placeholder="아이디를 입력하세요"
          >
        </div>
  
        <div class="form-group">
          <label for="password1">Password</label>
          <input 
            type="password" 
            id="password1" 
            v-model.trim="password1" 
            required 
            class="form-input"
            placeholder="비밀번호를 입력하세요"
          >
        </div>
  
        <div class="form-group">
          <label for="password2">Password Confirm</label>
          <input 
            type="password" 
            id="password2" 
            v-model.trim="password2" 
            required 
            class="form-input"
            placeholder="비밀번호를 다시 입력하세요"
          >
        </div>
  
        <button type="submit" class="signup-button">
          <span class="button-text">Start Adventure</span>
          <span class="star-icon">🚀</span>
        </button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { useAuthStore } from "@/stores/auth";
  
  const username = ref('');
  const password1 = ref('');
  const password2 = ref('');
  
  const store = useAuthStore();
  
  const signUp = async function () {
    try {
      const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value,
      };
      await store.signUp(payload);
    } catch (error) {
      console.error("회원가입 처리 중 오류:", error);
    }
  };
  </script>
  
  <style scoped>
  .signup-container {
    max-width: 400px;
    margin: auto;
    padding: 30px;
    border-radius: 15px;
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(240, 219, 55, 0.2);
    box-shadow: 
      0 8px 32px rgba(0, 0, 0, 0.3),
      inset 0 0 32px rgba(240, 219, 55, 0.05);
  }
  
  .signup-title {
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
    background: rgba(0, 0, 0, 0.2);
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
  
  .signup-button {
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
  }
  
  .signup-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
    background: linear-gradient(45deg, 
      rgba(240, 219, 55, 1), 
      rgba(255, 209, 4, 1)
    );
  }
  
  .star-icon {
    font-size: 18px;
  }
  </style>