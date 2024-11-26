<!-- StockRecommendationTable.vue -->
<template>
  <table>
    <thead>
      <tr>
        <th>종목코드</th>
        <th>종목명</th>
        <th>현재가</th>
        <th>등락률</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="stock in stocks" :key="stock.stock_id" >
        <td>{{ stock.stock_id }}</td>
        <td><span @click="goToNaverStock(stock.stock_id)">{{ stock.stock_name }}</span></td>
        <td>{{ stock.current_price }}원</td>
        <td :class="{ 'positive': stock.price_change_rate > 0, 'negative': stock.price_change_rate < 0 }">
          {{ stock.price_change_rate }}%
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
// 네이버 주식 종목 페이지로 이동
function goToNaverStock(stockId) {
  window.open(`https://finance.naver.com/item/main.nhn?code=${stockId}`, '_blank');
}

defineProps({
  stocks: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

tr:hover {
  background-color: #f5f5f5;
}

span {
  cursor: pointer;
  
}

.positive {
  color: red;
}

.negative {
  color: blue;
}
</style>