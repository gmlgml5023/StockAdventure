<template>
    <div>
      <!-- <h2>매매일지 작성</h2> -->
      <JournalCreateForm @create-complete="handleCreateComplete" />
    </div>
  </template>
  
  <script setup>
  import JournalCreateForm from '@/components/JournalCreateForm.vue'
  
  const handleCreateComplete = () => {
    console.log('매매일지가 작성되었습니다.')
  }
  </script>