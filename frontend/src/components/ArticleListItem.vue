<template>
  <div>
    <p>글번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>작성자 : {{ article.username }}</p>

    <RouterLink
      v-if="authStore.token"
      :to="{
        name: 'ArticleDetailView',
        params: { article_id: article.id },
      }"
      class="detail-btn"
    >
      상세보기
    </RouterLink>
    <hr />
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router"
import { useArticleStore } from '@/stores/article'
import { useAuthStore } from '@/stores/auth'

const articleStore = useArticleStore()
const authStore = useAuthStore()

defineProps({
  article: Object,
})
</script>

<style scoped>
.detail-btn {
  display: inline-block;
  padding: 8px 16px;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  margin: 10px 0;
}

.detail-btn:hover {
  background-color: #2980b9;
  transition: background-color 0.3s;
}
</style>