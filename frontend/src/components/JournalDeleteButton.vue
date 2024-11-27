<template>
  <button 
    @click="handleDelete"
    class="delete-button"
  >
    삭제하기 🗑️
  </button>
</template>
  
<script setup>
import { useJournalStore } from '@/stores/journal'
import { useRouter } from 'vue-router'

const props = defineProps({
  journalId: {  // journal 객체 대신 journalId만 받도록 수정
    type: [Number, String],
    required: true
  }
})

const emit = defineEmits(['delete-complete'])
const store = useJournalStore()
const router = useRouter()

const handleDelete = async () => {
  if (confirm('정말 삭제하시겠습니까?')) {
    try {
      await store.deleteJournal(props.journalId)
      emit('delete-complete')
      router.push({ name: 'JournalView' })
    } catch (error) {
      console.error('삭제 실패:', error)
    }
  }
}
</script>

<style scoped>
</style>