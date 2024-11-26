<template>
  <div class="profile-card">
    <div class="profile-header">
      <div class="profile-image">
        <img :src="characterImage" :alt="investmentStyle" />
      </div>
      <div class="profile-info">
        <h2 class="username">{{ profile_username }}</h2>
        <p class="investment-style">{{ investmentStyle }}</p>
      </div>
      <button @click="editProfile" class="menu-item edit-button">
        <span class="icon">✏️</span>
      </button>
    </div>
    <div class="resolution-container">
      <h3 class="resolution-title">투자 목표</h3>
      <p class="resolution" v-if="resolution">{{ resolution }}</p>
      <p class="resolution empty" v-else>투자 목표나 각오를 작성해주세요.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const props = defineProps({
  username: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(['edit-profile']);

const authStore = useAuthStore();
const token = authStore.token;

const profile_username = ref("");
const investmentStyle = ref("");
const characterImage = ref("");
const nickname = ref("");
const resolution = ref("");

import { useRoute, useRouter } from 'vue-router'
import UserProfile from '@/components/UserProfile.vue'

const route = useRoute()
const router = useRouter()
const username = route.params.username

const editProfile = () => {
  router.push(`/accounts/${username}/update`)
}

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

onMounted(() => {
  fetchProfile();
});
</script>

<style scoped>
.profile-card {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.3);
  border-radius: 20px;
  padding: 30px;
  width: 100%;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 30px;
  margin-bottom: 30px;
  position: relative;
}

.profile-image img {
  width: 120px;
  height: 120px;
  border-radius: 60px;
  object-fit: cover;
  border: 3px solid #f0db37;
  box-shadow: 0 0 20px rgba(240, 219, 55, 0.4);
}

.profile-info {
  flex-grow: 1;
}

.username {
  color: #f0db37;
  font-size: 32px;
  margin-bottom: 10px;
  text-shadow: 0 0 10px rgba(240, 219, 55, 0.6);
}

.investment-style {
  color: #fff;
  font-size: 18px;
  background: rgba(240, 219, 55, 0.2);
  padding: 5px 15px;
  border-radius: 20px;
  display: inline-block;
}

.edit-button {
  position: absolute;
  top: 0;
  right: 0;
  background: rgba(240, 219, 55, 0.2);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.edit-button:hover {
  background: rgba(240, 219, 55, 0.4);
}

.edit-button .icon {
  font-size: 20px;
}

.resolution-container {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  padding: 20px;
}

.resolution-title {
  color: #f0db37;
  font-size: 22px;
  margin-bottom: 15px;
}

.resolution {
  color: #fff;
  font-size: 18px;
  line-height: 1.6;
}

.resolution.empty {
  color: rgba(255, 255, 255, 0.6);
  font-style: italic;
}

@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
  }

  .profile-image img {
    width: 150px;
    height: 150px;
    border-radius: 75px;
  }

  .edit-button {
    position: static;
    margin-top: 20px;
  }
}
</style>