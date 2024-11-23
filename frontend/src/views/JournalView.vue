<template>
  <div>
    <div class="journal-header">
      <RouterLink 
        :to="{ name: 'CreateView' }" 
        class="create-button"
      >
        매매일지 작성
      </RouterLink>
    </div>
    <h2>매매일지 목록</h2>
    <JournalList/>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import {useJournalStore} from '@/stores/journal'
import JournalList from '@/components/JournalList.vue';

const store = useJournalStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getJournals()
})
</script>

<style>
.journal-header {
  margin-bottom: 20px;
}


.create-button:hover {
  background-color: #3aa876;
}
</style>