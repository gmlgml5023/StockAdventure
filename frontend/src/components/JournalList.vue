<template>
    <div>
      <JournalListItem 
        v-for="journal in store.journals"
        :key="journal.id"
        :journal="journal"
      />

    </div>
  </template>
  
  <script setup>
  import { useJournalStore } from '@/stores/journal'
  import JournalListItem from '@/components/JournalListItem.vue';
  
  const store = useJournalStore()
  </script>