<template>
  <div class="mypage">
    <div class="profile-section">
      <div class="profile-image">
        <img :src="characterImage" :alt="investmentStyle" />
      </div>
      <div class="profile-info">
        <h2>{{ profile_username }}</h2>
        <p class="investment-style">{{ investmentStyle }}</p>
        <p class="resolution" v-if="resolution">{{ resolution }}</p>
        <p class="resolution" v-else>각오가 아직 작성되지 않았습니다.</p>
      </div>
      <div class="button-group">
        <button @click="editProfile" class="edit-button">회원정보 수정</button>
        <router-link :to="{ name: 'user-journal', params: { username: props.username } }" class="journal-button">
          매매일지 목록
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

const authStore = useAuthStore();
const token = authStore.token;
const router = useRouter();


const profile_username = ref("");
const investmentStyle = ref("");
const characterImage = ref("");
const nickname = ref("");
const resolution = ref("");

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
    nickname.value = response.data.nickname;
    investmentStyle.value = response.data.investment_style;
    resolution.value = response.data.resolution;
    // 투자 스타일 ID에 따라 캐릭터 이미지 설정
    const styleId = response.data.image.split("_")[1].split(".")[0];
    // characterImage.value = `/images/${getCharacterImage(parseInt(styleId))}`;
    characterImage.value = response.data.image;

    console.log("Server response:", response.data);
    console.log("Style ID:", styleId);
    console.log("Character Image:", characterImage.value);
  } catch (error) {
    console.error("프로필 로딩 실패:", error);
  }
};

const editProfile = () => {
  // 회원정보 수정 페이지로 이동
  router.push(`/accounts/${props.username}/update`);
};

const goToJournalList = () => {
  // 매매일지 목록 페이지로 이동
  router.push('/journals/');
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

.resolution {
  color: #666;
  margin-top: 8px;
  font-size: 0.9em;
  line-height: 1.4;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.edit-button,
.journal-button {
  padding: 10px 20px;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.edit-button {
  background-color: #4caf50;
}

.journal-button {
  background-color: #2196F3;
}
</style>
