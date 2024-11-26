<template>
  <button @click="updateStocksData" :disabled="isUpdating" class="update-button">
    <span class="button-text">{{ buttonText }}</span>
    <span class="star-icon">{{ isUpdating ? '🚀' : '' }}</span>
  </button>
</template>

<script setup>
import { computed } from 'vue'
import { useStockStore } from '@/stores/stock'
import { storeToRefs } from 'pinia'

const stockStore = useStockStore()
const { isUpdating } = storeToRefs(stockStore)
const { updateStocks } = stockStore

const buttonText = computed(() => {
  return isUpdating.value ? '주식 탐사 중...' : '주식 정보 불러오기'
})

const updateStocksData = () => {
  updateStocks()
}
</script>

<style scoped>
.update-button {
  padding-top: 12px;
  padding-bottom: 12px;
  padding-left: 12px;
  border-radius: 8px;
  border: none;
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 0.9), 
    rgba(255, 209, 4, 0.9)
  );
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

.update-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}

.update-button:disabled {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(240, 219, 55, 0.4);
  color: rgba(240, 219, 55, 0.6);
  cursor: not-allowed;
  transform: none;
}

.star-icon {
  font-size: 18px;
}
</style>