<template>
    <button @click="updateStocksData" :disabled="isUpdating" class="update-button">
      {{ buttonText }}
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
    return isUpdating.value ? '업데이트 중...' : '주식 데이터 업데이트'
  })
  
  const updateStocksData = () => {
    updateStocks()
  }
  </script>
  
  <style scoped>
  .update-button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .update-button:hover {
    background-color: #45a049;
  }
  
  .update-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  </style>