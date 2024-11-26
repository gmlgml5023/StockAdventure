<template>
  <div class="article-container">
    <h1 class="article-title">Community Post</h1>
    <form @submit.prevent="handleSubmit" class="article-form">
      <div class="form-group">
        <label for="title">제목</label>
        <input 
          type="text" 
          id="title" 
          v-model.trim="formData.title" 
          required
          class="form-input"
          placeholder="제목을 입력하세요"
        >
      </div>

      <div class="form-group">
        <label for="article_content">내용</label>
        <textarea 
          id="article_content" 
          v-model.trim="formData.article_content"
          required
          class="form-textarea"
          placeholder="내용을 입력하세요"
        ></textarea>
      </div>

      <button type="submit" class="submit-button">
        <span class="button-text">Share Story</span>
        <span class="star-icon">✨</span>
      </button>
    </form>
  </div>
</template>
  
  <script setup>
  import { ref } from 'vue'
  import { useArticleStore } from '@/stores/article'
  import { useAuthStore } from '@/stores/auth'  // auth store import 추가
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const emit = defineEmits(['create-complete'])
  const articleStore = useArticleStore()
  const authStore = useAuthStore()  // auth store 사용
  const router = useRouter()
  
  const formData = ref({
    title: '',
    article_content: ''
  })
  
  const handleSubmit = async () => {
    // 제목과 내용 검증
    if (!formData.value.title.trim()) {
      alert('제목을 입력해주세요.')
      return
    }
    if (!formData.value.article_content.trim()) {
      alert('내용을 입력해주세요.')
      return
    }
  
    try {
      await axios({
        method: 'post',
        url: `${articleStore.API_URL}/articles/`,
        data: formData.value,
        headers: {
          Authorization: `Token ${authStore.token}`  // authStore에서 토큰 가져오기
        }
      })
      emit('create-complete')
      router.push({ name: 'ArticleView' })
    } catch (err) {
      console.error('게시글 작성 실패:', err)
      alert('게시글 작성에 실패했습니다.')  // 에러 메시지 추가
    }
  }
  </script>

<style scoped>
.article-container {
  max-width: 800px;
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

.article-title {
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
  min-height: 300px;
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

.submit-button {
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
  margin-top: 20px;
}

.submit-button:hover {
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