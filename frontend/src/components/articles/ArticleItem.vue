<template>
    <div class="article-item" @click="$emit('click')">
      <h3>{{ article.title }}</h3>
      <p class="content-preview">{{ contentPreview }}</p>
      <div class="meta">
        <span>작성일: {{ formatDate(article.created_at) }}</span>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    article: {
      type: Object,
      required: true
    }
  })
  
  const contentPreview = computed(() => {
    return props.article.article_content.slice(0, 100) + '...'
  })
  
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString()
  }
  </script>
  
  <style scoped>
  .article-item {
    padding: 15px;
    border-bottom: 1px solid #eee;
    cursor: pointer;
  }
  
  .article-item:hover {
    background-color: #f5f5f5;
  }
  
  .content-preview {
    color: #666;
    font-size: 0.9em;
  }
  
  .meta {
    font-size: 0.8em;
    color: #999;
  }
  </style>