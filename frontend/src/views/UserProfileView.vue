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
// // 이미지 설정
// const getCharacterImage = (styleId) => {
//   const investmentStyles = {
//     1: "character_stable.png",
//     2: "character_neutral.png",
//     3: "character_aggressive.png",
//   };
//   return investmentStyles[styleId] || "default_character.png";
// };

const editProfile = () => {
  // 회원정보 수정 페이지로 이동
  router.push(`/accounts/${props.username}/update`);
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

.edit-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
