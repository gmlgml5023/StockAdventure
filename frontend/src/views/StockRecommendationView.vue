<template>
  <div class="recommended-stocks">
    <h1 class="stock-title">오늘의 추천 종목</h1>
    <!-- <div class="header-section">
      <StockUpdateButton class="update-button" />
    </div> -->
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



  .stock-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 32px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

  .recommended-stocks {
    max-width: 1200px;
    margin: 20px auto;
    padding: 20px;


  }
  
  .header-section {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
  }
  
  .no-stocks {
    text-align: center;
    color: #f0db37;
    margin-top: 20px;
    padding: 20px;
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(240, 219, 55, 0.2);
    border-radius: 15px;
  }
  </style>