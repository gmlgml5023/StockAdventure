<template>
  <div>
    <h1>게시글 작성</h1>
    <ArticleCreateForm @create-complete="handleCreateComplete" />
  </div>
</template>

<script setup>
import ArticleCreateForm from '@/components/ArticleCreateForm.vue'

const handleCreateComplete = () => {
  console.log('게시글이 작성되었습니다.')
}
</script>