<template>
  <div class="journal-detail-container">
    <h1 class="detail-title">Trading Record</h1>
      <div v-if="!isEditing" class="journal-content">
        <div class="journal-header">
          <span class="journal-number">No. {{ journal.id }}</span>
          <span class="journal-type" :class="journal.buysell === '매수' ? 'buy' : 'sell'">
            {{ journal.buysell }}
          </span>
        </div>

        <div class="info-grid">
          <div class="info-item">
            <span class="info-label">종목명</span>
            <span class="info-value">{{ journal.stock_name }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">거래일자</span>
            <span class="info-value">{{ journal.transaction_date }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">거래수량</span>
            <span class="info-value">{{ journal.quantity }}주</span>
          </div>
          <div class="info-item">
            <span class="info-label">거래가격</span>
            <span class="info-value">{{ journal.price }}원</span>
          </div>
        </div>

        <div class="text-section">
          <div class="text-block">
            <h3>매매이유</h3>
            <p>{{ journal.reason }}</p>
          </div>
          <div class="text-block">
            <h3>피드백</h3>
            <p>{{ journal.feedback }}</p>
          </div>
        </div>
        
        <div class="button-group">
          <button @click="isEditing = true" class="edit-button">
            <span class="button-text">수정하기</span>
            <span class="star-icon">✏️</span>
          </button>
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

<style scoped>
.journal-detail-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.detail-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 32px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.detail-card {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.journal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.journal-number {
  color: #f0db37;
  font-size: 20px;
  font-weight: bold;
}

.journal-type {
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 16px;
  font-weight: bold;
}

.journal-type.buy {
  background: rgba(46, 213, 115, 0.2);
  color: #2ed573;
}

.journal-type.sell {
  background: rgba(255, 71, 87, 0.2);
  color: #ff4757;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 30px;
}

.info-item {
  background: rgba(240, 219, 55, 0.1);
  padding: 15px;
  border-radius: 8px;
}

.info-label {
  display: block;
  color: rgba(240, 219, 55, 0.7);
  font-size: 14px;
  margin-bottom: 5px;
}

.info-value {
  color: #f0db37;
  font-size: 18px;
  font-weight: bold;
}

.text-section {
  margin-bottom: 30px;
}

.text-block {
  margin-bottom: 20px;
}

.text-block h3 {
  color: #f0db37;
  margin-bottom: 10px;
  font-size: 18px;
}

.text-block p {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  background: rgba(0, 0, 0, 0.2);
  padding: 15px;
  border-radius: 8px;
}

.button-group {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}

.edit-button {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: none;
  background: linear-gradient(45deg, rgba(240, 219, 55, 0.9), rgba(255, 209, 4, 0.9));
  color: #000;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.edit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}

.star-icon {
  font-size: 18px;
}
</style>