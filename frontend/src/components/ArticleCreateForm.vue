<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="formData.title" required>
      </div>
      <div>
        <label for="article_content">내용 : </label>
        <textarea 
          id="article_content" 
          v-model.trim="formData.article_content"
          required
        ></textarea>
      </div>
      <input type="submit" value="작성">
    </form>
  </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useArticleStore } from '@/stores/article'
  import { useAuthStore } from '@/stores/auth'  // auth store import 추가
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const emit = defineEmits(['create-complete'])
  const articleStore = useArticleStore()
  const authStore = useAuthStore()  // auth store 사용
  const router = useRouter()
  
  const formData = ref({
    title: '',
    article_content: ''
  })
  
  const handleSubmit = async () => {
    // 제목과 내용 검증
    if (!formData.value.title.trim()) {
      alert('제목을 입력해주세요.')
      return
    }
    if (!formData.value.article_content.trim()) {
      alert('내용을 입력해주세요.')
      return
    }
  
    try {
      await axios({
        method: 'post',
        url: `${articleStore.API_URL}/articles/`,
        data: formData.value,
        headers: {
          Authorization: `Token ${authStore.token}`  // authStore에서 토큰 가져오기
        }
      })
      emit('create-complete')
      router.push({ name: 'ArticleView' })
    } catch (err) {
      console.error('게시글 작성 실패:', err)
      alert('게시글 작성에 실패했습니다.')  // 에러 메시지 추가
    }
  }
  </script>