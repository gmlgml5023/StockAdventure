<template>
  <div class="article-form">
    <h1>게시글 {{ isEdit ? '수정' : '작성' }}</h1>
    <article-form />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import ArticleForm from '@/components/articles/ArticleForm.vue'

const route = useRoute()
const isEdit = computed(() => !!route.params.id)
</script>