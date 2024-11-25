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
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const emit = defineEmits(['create-complete'])
  const store = useArticleStore()
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
      url: `${store.API_URL}/articles/`,
      data: formData.value,
    })
    emit('create-complete')
    router.push({ name: 'ArticleView' })
  } catch (err) {
    console.error('게시글 작성 실패:', err)
  }
}
</script>