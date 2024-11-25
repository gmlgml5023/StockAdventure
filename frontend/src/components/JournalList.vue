<template>
    <div>
      <JournalListItem 
        v-for="journal in userJournals"
        :key="journal.id"
        :journal="journal"
      />

    </div>
  </template>
  
  <script setup>
  import { useJournalStore } from '@/stores/journal'
  import { storeToRefs } from 'pinia'
  import JournalListItem from '@/components/JournalListItem.vue';
  
  const journalStore = useJournalStore()
  const { userJournals } = storeToRefs(journalStore)

  </script>