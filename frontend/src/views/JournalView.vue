<template>
  <div class="journal-container">
    <h1 class="journal-title">매매 일지</h1>
    <RouterLink :to="{ name: 'JournalCreateView' }" class="create-button">
      <span>쓰러 가기</span>
      <span class="star-icon">🚀</span>
    </RouterLink>
    <JournalList />
  </div>
</template>


<script setup>
import { onMounted } from "vue";
import { useJournalStore } from "@/stores/journal";
import JournalList from "@/components/JournalList.vue";

const store = useJournalStore();

onMounted(async () => {
  await store.getJournals();
  console.log('Journals loaded:', store.journals); // 디버깅을 위한 로그
});
</script>

<style scoped>
.journal-container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
}

.journal-title {
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