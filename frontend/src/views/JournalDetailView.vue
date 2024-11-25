<template>
  <div>
    <h2>매매일지 상세</h2>
    <div v-if="journal">
      <div v-if="!isEditing">
        <p>매매일지 No: {{ journal.id }}</p>
        <p>종목명: {{ journal.stock_name }}</p>
        <p>거래일자: {{ journal.transaction_date }}</p>
        <p>거래유형: {{ journal.buysell }}</p>
        <p>거래수량: {{ journal.quantity }}</p>
        <p>거래가격: {{ journal.price }}</p>
        <p>매매이유: {{ journal.reason }}</p>
        <p>피드백: {{ journal.feedback }}</p>
        
        <div class="button-group">
          <button @click="isEditing = true">수정</button>
          <JournalDeleteButton 
            :journal-id="journal.id"
            @delete-complete="handleDeleteComplete"
          />
        </div>
      </div>

      <JournalUpdateForm
        v-else
        :journal="journal"
        @update-complete="handleUpdateComplete"
        @cancel="isEditing = false"
      />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useJournalStore } from '@/stores/journal'
import { useRoute } from 'vue-router'
import JournalUpdateForm from '@/components/JournalUpdateForm.vue'
import JournalDeleteButton from '@/components/JournalDeleteButton.vue'
import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

const journalstore = useJournalStore()
const route = useRoute()
const journal = ref(null)
const isEditing = ref(false)
const authStore = useAuthStore()

const fetchJournal = async () => {
  try {
    const response = await axios.get(
      `${journalstore.API_URL}/journals/${route.params.journal_id}/`, {
      headers: {
        'Authorization': `Token ${authStore.token}` // 인증 토큰 추가
      }
  })
    journal.value = response.data
  } catch (error) {
    console.error('매매일지 로딩 실패:', error)
    console.log(authStore.token)
  }
}

onMounted(() => {
  const journalId = route.params.journal_id
  if (journalId) {
    fetchJournal(journalId)
  } else {
    console.error('Journal ID not found in route params')
  }
})

const handleUpdateComplete = async () => {
  await fetchJournal(route.params.journal_id)
  isEditing.value = false
}

const handleDeleteComplete = () => {
  journal.value = null
}
</script>