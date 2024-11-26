<template>
  <div class="journal-list">
    <div class="journal-grid">
      <JournalListItem 
        v-for="journal in userJournals"
        :key="journal.id"
        :journal="journal"
      />
    </div>
  </div>
</template>
  
<script setup>
import { useJournalStore } from '@/stores/journal'
import { storeToRefs } from 'pinia'
import JournalListItem from '@/components/JournalListItem.vue';

const journalStore = useJournalStore()
const { userJournals } = storeToRefs(journalStore)

</script>

<style scoped>
.journal-list {
  margin-top: 20px;
}

.journal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px 0;
}
</style>