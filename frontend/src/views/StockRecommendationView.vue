<!-- StockRecommendationView.vue -->
<template>
    <div class="recommended-stocks">
      <StockUpdateButton />
      <h2>추천 종목</h2>
      <StockRecommendationTable 
        v-if="stockStore.recommendedStocks.length > 0"
        :stocks="stockStore.recommendedStocks"
      />
      <div v-else class="no-stocks">
        주식 정보를 불러오기 전입니다. 정보 받아오기 버튼을 눌러주세요.
      </div>
    </div>
  </template>
  
  <script setup>
  import { useStockStore } from '@/stores/stock';
  import { onMounted } from 'vue';
  import StockRecommendationTable from '@/components/StockRecommendationTable.vue';
  import StockUpdateButton from '@/components/StockUpdateButton.vue';

  const stockStore = useStockStore();
  
  const loadRecommendedStocks = () => {
    stockStore.getRecommendedStocks();
  };
  
  onMounted(() => {
    loadRecommendedStocks();
  });
  </script>
  
  <style scoped>
  .recommended-stocks {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .no-stocks {
    text-align: center;
    color: #666;
    margin-top: 20px;
  }
  </style>