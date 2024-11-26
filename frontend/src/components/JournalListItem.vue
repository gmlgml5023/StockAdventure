<template>
  <div class="journal-card">
    <div class="journal-header">
      <!-- <span class="journal-number">No. {{ journal.id }}</span> -->
      <span class="journal-type" :class="journal.buysell === '매수' ? 'buy' : 'sell'">
        {{ journal.buysell }}
      </span>
    </div>
    
    <div class="journal-content">
      <div class="journal-date">
        <span class="icon">📅</span>
        {{ formatDate(journal.transaction_date) }}
      </div>
      
      <RouterLink
        :to="{
          name: 'JournalDetailView',
          params: { journal_id: journal.id },
        }"
        class="detail-button"
      >
        거래 내역 보기
        <span class="arrow">→</span>
      </RouterLink>
    </div>
  </div>
</template>
<script setup>
import { defineProps } from 'vue';

defineProps({
  journal: {
    type: Object,
    required: true,
  },
});

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
};
</script>

<style scoped>
.journal-card {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}

.journal-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 32px rgba(240, 219, 55, 0.1);
}

.journal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.journal-number {
  color: #f0db37;
  font-weight: bold;
}

.journal-type {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 14px;
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

.journal-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.journal-date {
  color: #f0db37;
  display: flex;
  align-items: center;
  gap: 8px;
}

.detail-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background: rgba(240, 219, 55, 0.1);
  border-radius: 8px;
  color: #f0db37;
  text-decoration: none;
  transition: all 0.3s ease;
}

.detail-button:hover {
  background: rgba(240, 219, 55, 0.2);
}

.arrow {
  font-size: 18px;
  transition: transform 0.3s ease;
}

.detail-button:hover .arrow {
  transform: translateX(5px);
}
</style>