<template>
  <div class="profile-view">
    <div class="content-wrapper">
      <UserProfile :username="username" />

      <div class="menu-container">
        <RouterLink to="/investment_style/test" class="menu-item">
          투자 성향 검사 다시 하기
        </RouterLink>
        <button @click="confirmLogOut" class="menu-item logout-button">
          로그 아웃
        </button>
        <button @click="withdrawAccount" class="menu-item withdraw-button">
          회원 탈퇴
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import UserProfile from '@/components/UserProfile.vue'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const username = route.params.username

const confirmLogOut = () => {
  if (confirm('정말 로그아웃하시겠습니까?')) {
    authStore.logOut();
  }
};

const withdrawAccount = async () => {
  if (confirm('정말로 회원 탈퇴하시겠습니까? 이 작업은 되돌릴 수 없습니다.')) {
    try {
      // 회원 탈퇴 API 호출
      await authStore.withdrawAccount()
      router.push('/login')
    } catch (error) {
      console.error('회원 탈퇴 실패:', error)
    }
  }
}
</script>

<style scoped>
.profile-view {
  min-height: 100vh;
  padding: 40px 20px;
  background: url('@/assets/space-background.jpg') no-repeat center center fixed;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.content-wrapper {
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.menu-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
  margin-top: 40px;
  width: 100%;
}

.menu-item {
  background-color: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  padding: 20px;
  text-align: center;
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 20px;
  transition: all 0.3s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(5px);
}

.menu-item:hover {
  background-color: rgba(255, 255, 255, 0.2);
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.logout-button {
  background-color: rgba(255, 193, 7, 0.2);
  border-color: rgba(255, 193, 7, 0.4);
  color: #ffc107;
}

.logout-button:hover {
  background-color: rgba(255, 193, 7, 0.3);
  box-shadow: 0 10px 20px rgba(255, 193, 7, 0.2);
}

.withdraw-button {
  background-color: rgba(220, 53, 69, 0.2);
  border-color: rgba(220, 53, 69, 0.4);
  color: #dc3545;
}

.withdraw-button:hover {
  background-color: rgba(220, 53, 69, 0.3);
  box-shadow: 0 10px 20px rgba(220, 53, 69, 0.2);
}

@media (max-width: 768px) {
  .menu-container {
    grid-template-columns: 1fr;
  }
}
</style>