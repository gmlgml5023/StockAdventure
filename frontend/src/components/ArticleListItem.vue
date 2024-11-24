<template>
  <div>
    <p>글번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>

    <RouterLink
      :to="{
        name: 'ArticleDetailView',
        params: { article_id: article.id },
      }"
    >
      Detail
    </RouterLink>
    <hr />
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  article: Object,
});
</script>
