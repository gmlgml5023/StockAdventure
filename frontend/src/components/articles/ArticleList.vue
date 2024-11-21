<template>
    <div class="article-list">
      <h2>게시글 목록</h2>
      <div v-if="loading">Loading...</div>
      <div v-else>
        <article-item
          v-for="article in articles"
          :key="article.id"
          :article="article"
          @click="goToDetail(article.id)"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { useArticleStore } from '@/stores/article'
  import ArticleItem from './ArticleItem.vue'
  
  const router = useRouter()
  const store = useArticleStore()
  const loading = ref(true)
  const articles = ref([])
  
  onMounted(async () => {
    try {
      await store.fetchArticles()
      articles.value = store.articles
    } finally {
      loading.value = false
    }
  })
  
  const goToDetail = (id) => {
    router.push({ name: 'article-detail', params: { id } })
  }
  </script>
  
  <style scoped>
  .article-list {
    padding: 20px;
  }
  </style>