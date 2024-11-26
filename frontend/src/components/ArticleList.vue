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