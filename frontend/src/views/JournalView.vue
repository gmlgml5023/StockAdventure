<template>
  <div>
    <h2>매매일지 목록</h2>
    <RouterLink :to="{ name: 'JournalCreateView' }" class="create-button">매매일지 작성</RouterLink>
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

<style>
.create-button:hover {
  background-color: #3aa876;
}
</style>
