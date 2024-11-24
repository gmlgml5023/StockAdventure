<template>
  <div>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
</script>
