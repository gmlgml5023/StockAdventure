<template>
  <div class="article-list">
    <div class="article-grid">
      <ArticleListItem 
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
      />
    </div>
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
</script>

<style scoped>
.article-list {
  margin-top: 20px;
}

.article-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px 0;
}
</style>

<!-- 한줄에 하나씩 길게 배치 코드 -->
<!-- <style scoped>
.article-list {
  margin-top: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.article-grid {
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 20px 0;
}
</style> -->