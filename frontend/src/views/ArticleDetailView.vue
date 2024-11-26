<template>
  <div class="article-detail-container">
      <!-- <h1 class="detail-title">Detail</h1> -->

      <button @click="$router.go(-1)" class="back-button">
        <span class="button-text">돌아가기</span>
        <span class="star-icon">🚀</span>
      </button>

    <div v-if="article" class="detail-card">
      <div v-if="!isEditing">
        <div class="article-header">
          <h2 class="article-title">{{ article.title }}</h2>
          <div class="article-meta">
            <span>작성자: {{ article.username }}</span>
            <span>작성일: {{ article.created_at }}</span>
            <span>수정일: {{ article.updated_at }}</span>
          </div>
        </div>

        <div class="article-content">
          {{ article.article_content }}
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
    <div v-else class="loading-message">
      게시글을 불러오는 중입니다...
    </div>
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
</script>

<style scoped>

/* 돌아가기 버튼과 제목을 감싸는 컨테이너 */
.article-detail-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

/* 돌아가기 버튼 스타일 */
.back-button {
  display: flex;
  align-items: center;
  padding: 12px 24px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background: rgba(0, 0, 0, 0.3);
  color: #f0db37;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  gap: 10px;
  backdrop-filter: blur(15px);
  margin-left: auto; /* 오른쪽 정렬을 위해 추가 */
  margin-bottom: 20px; /* 아래 여백 추가 */
}

.back-button:hover {
  transform: translateX(5px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
  background: rgba(240, 219, 55, 0.1);
}

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

/* 게시글 헤더 영역 */
.article-header {
  border-bottom: 1px solid rgba(240, 219, 55, 0.2);
  padding-bottom: 20px;
  margin-bottom: 20px;
}

/* 제목 스타일 */
.article-title {
  color: #f0db37;
  font-size: 24px;
  margin-bottom: 15px;
}

/* 메타 정보 스타일 */
.article-meta {
  display: flex;
  justify-content: space-between;
  color: rgba(240, 219, 55, 0.7);
  font-size: 14px;
}

/* 게시글 본문 */
.article-content {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  padding: 20px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  margin: 20px 0;
  min-height: 200px;
}

.article-info {
  display: flex;
  padding: 12px;
  border-bottom: 1px solid rgba(240, 219, 55, 0.1);
}

.article-info-label {
  color: rgba(240, 219, 55, 0.7);
  width: 100px;
  flex-shrink: 0;
}

.article-info-value {
  color: rgba(255, 255, 255, 0.8);
  flex-grow: 1;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid rgba(240, 219, 55, 0.2);
}

.edit-button {
  padding: 12px 24px;
  /* border-radius: 8px; */
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
  gap: 10px;
}

.edit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}
</style>