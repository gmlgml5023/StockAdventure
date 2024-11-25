<template>
  <div class="update-profile">
    <h2>회원정보 수정</h2>
    <form @submit.prevent="updateProfile" class="update-form">
      <div class="form-group">
        <label for="nickname">닉네임</label>
        <input
          type="text"
          id="nickname"
          v-model="profileData.nickname"
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label for="resolution">자기소개</label>
        <textarea
          id="resolution"
          v-model="profileData.resolution"
          class="form-input"
          rows="4"
        ></textarea>
      </div>

      <div class="button-group">
        <button type="submit" class="submit-button">저장</button>
        <button type="button" @click="goBack" class="cancel-button">
          취소
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";

const router = useRouter();
const authStore = useAuthStore();
const token = authStore.token;

const props = defineProps({
  username: {
    type: String,
    required: true,
  },
});

const profileData = ref({
  nickname: "",
  resolution: "",
  investment_style: "",
  image: null,
});

// 프로필 정보 가져오기
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
    profileData.value = {
      nickname: response.data.nickname,
      resolution: response.data.resolution,
      investment_style: response.data.investment_style,
    };
  } catch (error) {
    console.error("프로필 로딩 실패:", error);
  }
};

// 이미지 파일 처리
const handleImageChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    profileData.value.image = file;
  }
};

// 프로필 업데이트
const updateProfile = async () => {
  try {
    const formData = new FormData();
    formData.append("nickname", profileData.value.nickname);
    formData.append("resolution", profileData.value.resolution);
    if (profileData.value.image) {
      formData.append("image", profileData.value.image);
    }

    await axios.put(
      `http://127.0.0.1:8000/accounts/${props.username}/update/`,
      formData,
      {
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "multipart/form-data",
        },
      }
    );

    router.push(`/accounts/${props.username}`);
  } catch (error) {
    console.error("프로필 업데이트 실패:", error);
  }
};

const goBack = () => {
  router.push(`/accounts/${props.username}`);
};

onMounted(() => {
  fetchProfile();
});
</script>

<style scoped>
.update-profile {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.update-form {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-top: 5px;
}

.investment-style {
  color: #666;
  margin: 5px 0;
}

small {
  color: #666;
  font-size: 0.8em;
}

.button-group {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.submit-button,
.cancel-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button {
  background-color: #4caf50;
  color: white;
}

.cancel-button {
  background-color: #f44336;
  color: white;
}
</style>
