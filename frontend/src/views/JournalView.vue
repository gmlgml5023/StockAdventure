<template>
  <div class="journal-container">
    <h1 class="journal-title">매매 일지</h1>
    <RouterLink :to="{ name: 'JournalCreateView' }" class="create-button">
      <span>작성하기</span>
      <span class="star-icon">🚀</span>
    </RouterLink>
    <div v-if="store.journals.length === 0" class="empty-state">
      <span class="empty-icon">📝</span>
      <p class="empty-text">작성된 매매일지가 없습니다.</p>
      <p class="empty-subtext">우측 상단의 작성하기 버튼을 눌러 첫 매매일지를 작성해보세요!</p>
    </div>
    <JournalList v-else />
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

.empty-state {
  background: linear-gradient(45deg, rgba(240, 219, 55, 0.1), rgba(255, 209, 4, 0.1));
  border: 2px solid rgba(240, 219, 55, 0.3);
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  margin: 40px auto;
}

.empty-icon {
  font-size: 48px;
  display: block;
  margin-bottom: 20px;
}

.empty-text {
  color: #f0db37;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
  text-shadow: 0 0 10px rgba(240, 219, 55, 0.3);
}

.empty-subtext {
  color: #a8a8a8;
  font-size: 16px;
}
</style>