<template>
  <div class="mypage">
    <div class="profile-section">
      <div class="profile-image">
        <img :src="characterImage" :alt="investmentStyle" />
      </div>
      <div class="profile-info">
        <h2>{{ profile_username }}</h2>
        <p class="investment-style">{{ investmentStyle }}</p>
      </div>
      <button @click="editProfile" class="edit-button">회원정보 수정</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const token = authStore.token;
const profile_username = ref("");
const investmentStyle = ref("");
const characterImage = ref("");
const router = useRouter();

const props = defineProps({
  username: {
    type: String,
    required: true,
  },
});

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
    investmentStyle.value = response.data.investment_style;
    characterImage.value = `/images/${response.data.character_image}`;
  } catch (error) {
    console.error("프로필 로딩 실패:", error);
  }
};

const editProfile = () => {
  // 회원정보 수정 페이지로 이동
  router.push(`/accounts/${props.username}/update/`);
};

onMounted(() => {
  fetchProfile();
});
</script>

<style scoped>
.mypage {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.profile-section {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-image img {
  width: 120px;
  height: 120px;
  border-radius: 60px;
  object-fit: cover;
}

.profile-info {
  flex-grow: 1;
}

.investment-style {
  color: #666;
  margin-top: 8px;
}

.edit-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
