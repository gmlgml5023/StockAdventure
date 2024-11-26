<template>
    <div class="mypage">
      <div class="profile-section">
        <div class="profile-image">
          <img :src="characterImage" :alt="investmentStyle" />
        </div>
        <div class="profile-info">
          <h2 class="username">{{ profile_username }}</h2>
          <p class="investment-style">{{ investmentStyle }}</p>
          <p class="resolution" v-if="resolution">{{ resolution }}</p>
          <p class="resolution" v-else>아직 우주 여행의 목표가 설정되지 않았습니다.</p>
        </div>
        <div class="button-group">
          <button @click="editProfile" class="edit-button">
            <span class="button-text">프로필 수정</span>
            <span class="star-icon">✏️</span>
          </button>
          <router-link :to="{ name: 'user-journal', params: { username } }" class="journal-button">
            <span class="button-text">매매일지 보기</span>
            <span class="star-icon">📚</span>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import axios from "axios";
  import { useAuthStore } from "@/stores/auth";
  import { useRouter } from "vue-router";
  
  const props = defineProps({
    username: {
      type: String,
      required: true,
    },
  });
  
  const authStore = useAuthStore();
  const token = authStore.token;
  const router = useRouter();
  
  const profile_username = ref("");
  const investmentStyle = ref("");
  const characterImage = ref("");
  const nickname = ref("");
  const resolution = ref("");
  
  const fetchProfile = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/accounts/${props.username}/`,
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      );
      profile_username.value = response.data.username;
      nickname.value = response.data.nickname;
      investmentStyle.value = response.data.investment_style;
      resolution.value = response.data.resolution;
      characterImage.value = response.data.image;
    } catch (error) {
      console.error("프로필 로딩 실패:", error);
    }
  };
  
  const editProfile = () => {
    router.push(`/accounts/${props.username}/update`);
  };
  
  onMounted(() => {
    fetchProfile();
  });
  </script>
  
  <style scoped>
  .mypage {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
  }
  
  .profile-section {
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(240, 219, 55, 0.2);
    border-radius: 15px;
    padding: 30px;
    display: flex;
    align-items: center;
    gap: 30px;
    box-shadow: 
      0 8px 32px rgba(0, 0, 0, 0.3),
      inset 0 0 32px rgba(240, 219, 55, 0.05);
  }
  
  .profile-image {
    position: relative;
  }
  
  .profile-image img {
    width: 150px;
    height: 150px;
    border-radius: 75px;
    object-fit: cover;
    border: 2px solid rgba(240, 219, 55, 0.4);
    box-shadow: 0 0 20px rgba(240, 219, 55, 0.2);
  }
  
  .profile-info {
    flex-grow: 1;
  }
  
  .username {
    color: #f0db37;
    font-size: 28px;
    margin-bottom: 15px;
    text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
  }
  
  .investment-style {
    color: rgba(240, 219, 55, 0.9);
    font-size: 18px;
    margin-bottom: 10px;
    padding: 5px 15px;
    background: rgba(240, 219, 55, 0.1);
    border-radius: 20px;
    display: inline-block;
  }
  
  .resolution {
    color: rgba(255, 255, 255, 0.8);
    font-size: 16px;
    line-height: 1.6;
    margin-top: 15px;
    padding: 15px;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
  }
  
  .button-group {
    display: flex;
    flex-direction: column;
    gap: 15px;
    min-width: 160px;
  }
  
  .edit-button,
  .journal-button {
    padding: 12px;
    border-radius: 8px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    text-decoration: none;
  }
  
  .edit-button {
    background: linear-gradient(45deg, 
      rgba(240, 219, 55, 0.9), 
      rgba(255, 209, 4, 0.9)
    );
    color: #000;
  }
  
  .journal-button {
    background: rgba(255, 255, 255, 0.1);
    color: #f0db37;
    border: 1px solid rgba(240, 219, 55, 0.4);
  }
  
  .edit-button:hover,
  .journal-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
  }
  
  .star-icon {
    font-size: 18px;
  }
  
  @media (max-width: 768px) {
    .profile-section {
      flex-direction: column;
      text-align: center;
    }
  
    .button-group {
      width: 100%;
    }
  }
  </style>