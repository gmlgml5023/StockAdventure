<template>
    <div class="article-detail">
      <h2>{{ article.title }}</h2>
      <div class="meta">
        <span>작성일: {{ formatDate(article.created_at) }}</span>
        <span>수정일: {{ formatDate(article.updated_at) }}</span>
      </div>
      <div class="content">
        {{ article.article_content }}
      </div>
      <div class="actions">
        <button @click="editArticle">수정</button>
        <button @click="deleteArticle" class="delete">삭제</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { useArticleStore } from '@/stores/article'
  
  const props = defineProps({
    article: {
      type: Object,
      required: true
    }
  })
  
  const router = useRouter()
  const store = useArticleStore()
  
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString()
  }
  
  const editArticle = () => {
    router.push({ 
      name: 'article-edit', 
      params: { id: props.article.id }
    })
  }
  
  const deleteArticle = async () => {
    if (confirm('정말 삭제하시겠습니까?')) {
      await store.deleteArticle(props.article.id)
      router.push({ name: 'article-list' })
    }
  }
  </script>
  
  <style scoped>
  .article-detail {
    padding: 20px;
  }
  
  .meta {
    color: #666;
    margin: 10px 0;
  }
  
  .meta span {
    margin-right: 15px;
  }
  
  .content {
    margin: 20px 0;
    line-height: 1.6;
  }
  
  .actions {
    margin-top: 20px;
  }
  
  button {
    margin-right: 10px;
    padding: 8px 15px;
  }
  
  .delete {
    background-color: #ff4444;
    color: white;
    border: none;
  }
  </style>