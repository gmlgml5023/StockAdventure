<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <div v-if="!isEditing">
        <p>게시글 번호 : {{ article.id }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.article_content }}</p>
        <p>작성일 : {{ article.created_at }}</p>
        <p>수정일 : {{ article.updated_at }}</p>
        
        <!-- 작성자와 현재 로그인한 사용자가 같은 경우에만 버튼 그룹 표시 -->
        <div class="button-group" v-if="authStore.username === article.username">
          <button @click="isEditing = true">수정</button>
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