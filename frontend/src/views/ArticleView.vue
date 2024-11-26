<template>
  <div class="article-container">
    <h1 class="article-title">종목 토론 게시판</h1>
    <RouterLink :to="{ name: 'ArticleCreateView' }" class="create-button">
      <span>글 쓰러 가기</span>
      <span class="star-icon">✨</span>
    </RouterLink>
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


<style scoped>
.article-container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
}

.article-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 32px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.create-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: linear-gradient(45deg, rgba(240, 219, 55, 0.9), rgba(255, 209, 4, 0.9));
  color: #000;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  margin-bottom: 20px;
  margin-left: auto; /* 오른쪽 정렬을 위해 추가 */
  transition: all 0.3s ease;
  width: fit-content;
}

.create-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}

.star-icon {
  font-size: 18px;
}
</style>