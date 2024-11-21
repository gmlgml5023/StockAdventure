<template>
    <div class="article-form">
      <h2>{{ isEdit ? '게시글 수정' : '새 게시글 작성' }}</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="title">제목</label>
          <input
            id="title"
            v-model="formData.title"
            type="text"
            required
            placeholder="제목을 입력하세요"
          >
        </div>
        
        <div class="form-group">
          <label for="content">내용</label>
          <textarea
            id="content"
            v-model="formData.article_content"
            required
            placeholder="내용을 입력하세요"
            rows="10"
          ></textarea>
        </div>
  
        <div class="form-actions">
          <button type="submit">{{ isEdit ? '수정하기' : '작성하기' }}</button>
          <button type="button" @click="cancel">취소</button>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { useRouter } from 'vue-router'
  import { useArticleStore } from '@/stores/article'
  
  const props = defineProps({
    articleId: {
      type: Number,
      default: null
    }
  })
  
  const router = useRouter()
  const store = useArticleStore()
  
  const formData = ref({
    title: '',
    article_content: ''
  })
  
  const isEdit = computed(() => !!props.articleId)
  
  const handleSubmit = async () => {
    try {
      if (isEdit.value) {
        await store.updateArticle(props.articleId, formData.value)
      } else {
        await store.createArticle(formData.value)
      }
      router.push({ name: 'article-list' })
    } catch (error) {
      console.error('Failed to save article:', error)
    }
  }
  
  const cancel = () => {
    router.back()
  }
  </script>
  
  <style scoped>
  .article-form {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input, textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .form-actions {
    margin-top: 20px;
  }
  
  button {
    margin-right: 10px;
    padding: 8px 15px;
  }
  </style>