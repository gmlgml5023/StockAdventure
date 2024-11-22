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
        
        <div class="button-group">
          <button @click="isEditing = true">수정</button>
          <ArticleDeleteButton 
            :article-id="article.id"
            @delete-complete="handleDeleteComplete"
          />
        </div>
      </div>

      <ArticleUpdateForm
        v-else
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
import { useRoute } from 'vue-router'
import ArticleUpdateForm from '@/components/ArticleUpdateForm.vue'
import ArticleDeleteButton from '@/components/ArticleDeleteButton.vue'
import axios from 'axios'

const store = useArticleStore()
const route = useRoute()
const article = ref(null)
const isEditing = ref(false)

onMounted(() => {
  fetchArticle()
})

const fetchArticle = async () => {
  try {
    const response = await axios.get(
      `${store.API_URL}/articles/${route.params.article_id}/`
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