<template>
  <div class="article-card">
    <div class="article-header">
      <span class="article-number">No. {{ article.id }}</span>
      <span class="article-author">{{ article.username }}</span>
    </div>
    
    <div class="article-content">
      <h3 class="article-title">{{ article.title }}</h3>
      
      <RouterLink
        v-if="authStore.token"
        :to="{
          name: 'ArticleDetailView',
          params: { article_id: article.id },
        }"
        class="detail-button"
      >
        자세히 보기
        <span class="arrow">→</span>
      </RouterLink>
    </div>
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
.article-card {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}

.article-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 32px rgba(240, 219, 55, 0.1);
}

.article-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}

.article-number {
  color: #a1a09c;
  font-weight: lighter;
  font-size: 18px;
}

.article-author {
  color: #a1a09c;
  font-size: 15px;
}

.article-title {
  color: #f0db37;
  margin: 0 0 15px 0;
  font-size: 18px;
}

.detail-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background: rgba(152, 149, 125, 0.1);
  border-radius: 8px;
  color: #a1a09c;
  text-decoration: none;
  transition: all 0.3s ease;
}

.detail-button:hover {
  background: rgba(240, 219, 55, 0.2);
}

.arrow {
  font-size: 18px;
  transition: transform 0.3s ease;
}

.detail-button:hover .arrow {
  transform: translateX(5px);
}
</style>