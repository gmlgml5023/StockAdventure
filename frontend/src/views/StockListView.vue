// src/views/StockList.vue
<template>
  <div class="stock-container">
    <h1 class="stock-title">주식 정보 조회</h1>
    <div class="header-section">
      <StockUpdateButton class="update-button" />
    </div>
    <div v-if="!stockStore.stocks.length" class="loading-message">
      주식 데이터를 불러오기 전입니다.
    </div>
    <StockTable 
      v-else
      :stocks="stockStore.stocks"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useStockStore } from '@/stores/stock'
import StockTable from '@/components/StockTable.vue'
import StockUpdateButton from '@/components/StockUpdateButton.vue'

const stockStore = useStockStore()

onMounted(() => {
  stockStore.getStocks()
})
</script>

<style scoped>

.stock-container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
}


.stock-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 32px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.loading-message {
  text-align: center;
  padding: 40px;
  font-size: 16px;
  color: #666;
}

.header-section {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
  }
</style>