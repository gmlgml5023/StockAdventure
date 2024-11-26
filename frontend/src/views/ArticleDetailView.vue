<template>
  <div class="article-detail-container">
    <h1 class="detail-title">Space Story</h1>

      <div v-if="!isEditing">
        <div class="article-header">
          <span class="article-number">No. {{ article.id }}</span>
          <span class="article-date">
            <span class="date-label">작성일:</span> {{ formatDate(article.created_at) }}
            <span class="date-label">수정일:</span> {{ formatDate(article.updated_at) }}
          </span>
        </div>

        <div class="content-section">
          <h2 class="content-title">{{ article.title }}</h2>
          <p class="content-text">{{ article.article_content }}</p>
        </div>
        
        <div class="button-group" v-if="authStore.username === article.username">
          <button @click="isEditing = true" class="edit-button">
            <span class="button-text">수정하기</span>
            <span class="star-icon">✏️</span>
          </button>
          <ArticleDeleteButton 
            :article-id="article.id"
            @delete-complete="handleDeleteComplete"
          />
        </div>
      </div>

      <ArticleUpdateForm
        v-else-if="authStore.username === article.username"
        :article="article"
        @update-complete="handleUpdateComplete"
        @cancel="isEditing = false"
      />

  </div>
</template>


<script setup>
import { onMounted, ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useAuthStore } from '@/stores/auth'  // auth store import 추가
import { useRoute } from 'vue-router'
import ArticleUpdateForm from '@/components/ArticleUpdateForm.vue'
import ArticleDeleteButton from '@/components/ArticleDeleteButton.vue'
import axios from 'axios'

const articleStore = useArticleStore()
const authStore = useAuthStore()  // auth store 사용
const route = useRoute()
const article = ref(null)
const isEditing = ref(false)

onMounted(() => {
  fetchArticle()
})

const fetchArticle = async () => {
  try {
    const response = await axios.get(
      `${articleStore.API_URL}/articles/${route.params.article_id}/`,
      {
        headers: {
          Authorization: `Token ${authStore.token}`  // 토큰 추가
        }
      }
    )
    article.value = response.data
  } catch (error) {
    console.error('게시글 로딩 실패:', error)
  }
}

const handleUpdateComplete = async () => {
  await fetchArticle()
  isEditing.value = false
}

const handleDeleteComplete = () => {
  article.value = null
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};
</script>

<style scoped>
.article-detail-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.detail-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 32px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.detail-card {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.article-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba(240, 219, 55, 0.2);
}

.article-number {
  color: #f0db37;
  font-size: 20px;
  font-weight: bold;
}

.article-date {
  color: rgba(240, 219, 55, 0.7);
  font-size: 14px;
}

.date-label {
  margin: 0 10px;
  color: rgba(240, 219, 55, 0.5);
}

.content-section {
  margin-bottom: 30px;
}

.content-title {
  color: #f0db37;
  font-size: 24px;
  margin-bottom: 20px;
}

.content-text {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  white-space: pre-wrap;
  background: rgba(0, 0, 0, 0.2);
  padding: 20px;
  border-radius: 8px;
}

.button-group {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}

.edit-button {
  flex: 1;
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

.edit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}

.star-icon {
  font-size: 18px;
}
</style>