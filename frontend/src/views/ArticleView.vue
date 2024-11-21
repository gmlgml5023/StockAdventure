<template>
    <div>
      <h1>Article Page</h1>
      <RouterLink :to="{ name: 'CreateView' }">Create</RouterLink>
      <ArticleList />
    </div>
  </template>
  
  <script setup>
  import ArticleList from '@/components/ArticleList.vue'
  import { onMounted } from 'vue'
  import { useArticleStore } from '@/stores/article'
  import { RouterLink } from 'vue-router'
  
  const store = useArticleStore()
  
  onMounted(() => {
    // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
    store.getArticles()
  })
  </script>
  
  <style>
  
  </style>
  