<template>
    <button 
      @click="handleDelete"
      class="delete-button"
    >
      삭제
    </button>
  </template>
  
  <script setup>
  import { useArticleStore } from '@/stores/article'
  import { useRouter } from 'vue-router'
  
  const props = defineProps({
    articleId: {  // article 객체 대신 articleId만 받도록 수정
      type: [Number, String],
      required: true
    }
  })
  
  const emit = defineEmits(['delete-complete'])
  const store = useArticleStore()
  const router = useRouter()
  
  const handleDelete = async () => {
    if (confirm('정말 삭제하시겠습니까?')) {
      try {
        await store.deleteArticle(props.articleId)
        emit('delete-complete')
        router.push({ name: 'ArticleView' })
      } catch (error) {
        console.error('삭제 실패:', error)
      }
    }
  }
  </script>