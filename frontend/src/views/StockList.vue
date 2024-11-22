// src/views/StockList.vue
<template>
  <div class="stock-container">
    <h2>주식 종목 목록</h2>
    <div v-if="!stockStore.stocks.length" class="loading-message">
      주식 데이터를 불러오는 중입니다...
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

const stockStore = useStockStore()

onMounted(() => {
  stockStore.getStocks()
})
</script>

<style scoped>
.stock-container {
  padding: 20px;
}

.loading-message {
  text-align: center;
  padding: 40px;
  font-size: 16px;
  color: #666;
}
</style>