<template>
    <div class="update-profile">
      <h1 class="profile-title">Profile Update</h1>
      <form @submit.prevent="updateProfile" class="profile-form">
        <div class="form-group">
          <label for="nickname">닉네임</label>
          <input
            type="text"
            id="nickname"
            v-model="profileData.nickname"
            class="form-input"
            placeholder="닉네임을 입력하세요"
          />
        </div>
  
        <div class="form-group">
          <label for="resolution">각오 한 마디 !</label>
          <textarea
            id="resolution"
            v-model="profileData.resolution"
            class="form-textarea"
            placeholder="각오를 입력하세요"
            rows="4"
          ></textarea>
        </div>
  
        <div class="button-group">
          <button type="submit" class="submit-button">
            <span class="button-text">Save Changes</span>
            <span class="star-icon">💫</span>
          </button>
          <button type="button" @click="goBack" class="cancel-button">
            <span class="button-text">Cancel</span>
            <span class="star-icon">✖</span>
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
  
  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      profileData.value.image = file;
    }
  };
  
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
  
  .profile-title {
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
  
  .form-input, .form-textarea {
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
  
  .form-textarea {
    min-height: 120px;
    resize: vertical;
  }
  
  .form-input::placeholder,
  .form-textarea::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }
  
  .form-input:focus,
  .form-textarea:focus {
    outline: none;
    border-color: #f0db37;
    box-shadow: 0 0 15px rgba(240, 219, 55, 0.2);
    background: rgba(0, 0, 0, 0.3);
  }
  
  .button-group {
    display: flex;
    gap: 15px;
    margin-top: 20px;
  }
  
  .submit-button, .cancel-button {
    flex: 1;
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
  }
  
  .submit-button {
    background: linear-gradient(45deg, 
      rgba(240, 219, 55, 0.9), 
      rgba(255, 209, 4, 0.9)
    );
    color: #000;
  }
  
  .cancel-button {
    background: rgba(255, 255, 255, 0.1);
    color: #f0db37;
    border: 1px solid rgba(240, 219, 55, 0.4);
  }
  
  .submit-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
  }
  
  .cancel-button:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
  }
  
  .star-icon {
    font-size: 18px;
  }
  </style>