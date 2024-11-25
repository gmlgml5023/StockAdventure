<template>
  <div>
    <h2>커뮤니티</h2>
    <RouterLink :to="{ name: 'ArticleCreateView' }" class="create-button">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/article";
import ArticleList from "@/components/ArticleList.vue";

const store = useArticleStore();

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getArticles();
});
</script>


<style>
.create-button:hover {
  background-color: #3aa876;
}
</style>

