<template>
  <div class="recommendation-container">
    <table class="stock-table">
      <thead>
        <tr>
          <th>종목코드</th>
          <th>종목명</th>
          <th>현재가</th>
          <th>등락률</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stock in stocks" :key="stock.stock_id" class="stock-row">
          <td>{{ stock.stock_id }}</td>
          <td>
            <span @click="goToNaverStock(stock.stock_id)" class="stock-name">
              {{ stock.stock_name }}
              <span class="link-icon">🔗</span>
            </span>
          </td>
          <td class="number">{{ formatPrice(stock.current_price) }}원</td>
          <td class="number" :class="getPriceChangeClass(stock.price_change_rate)">
            {{ formatPercent(stock.price_change_rate) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
function goToNaverStock(stockId) {
  window.open(`https://finance.naver.com/item/main.nhn?code=${stockId}`, '_blank');
}

const formatPrice = (value) => {
  if (!value) return '-'
  return new Intl.NumberFormat('ko-KR').format(value)
}

const formatPercent = (value) => {
  if (!value) return '-'
  return (value > 0 ? '+' : '') + value.toFixed(2) + '%'
}

const getPriceChangeClass = (value) => {
  if (!value || value === 0) return 'neutral'
  return value > 0 ? 'up' : 'down'
}

defineProps({
  stocks: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
.recommendation-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 10px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  border-radius: 15px;
}

.stock-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}

.stock-table th {
  padding: 15px;
  background: rgba(0, 0, 0, 0.8);
  color: #f0db37;
  font-weight: bold;
  text-align: left;
  border-bottom: 2px solid rgba(240, 219, 55, 0.2);
}

.stock-table td {
  padding: 15px;
  background: rgba(0, 0, 0, 0.3);
  color: rgba(255, 255, 255, 0.8);
  border-bottom: 1px solid rgba(240, 219, 55, 0.1);
}

.stock-row {
  transition: all 0.3s ease;
}

.stock-row:hover td {
  background: rgba(240, 219, 55, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.1);
}

.stock-name {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: #f0db37;
  transition: all 0.3s ease;
}

.link-icon {
  opacity: 0;
  transition: all 0.3s ease;
  font-size: 14px;
}

.stock-name:hover {
  text-decoration: underline;
}

.stock-name:hover .link-icon {
  opacity: 1;
}

.number {
  text-align: right;
}

/* 가격 변동 색상 수정 */
.up {
  color: #ff4757 !important; /* 빨간색 */
  font-weight: bold;
}

.down {
  color: #1261c4 !important; /* 파란색 */
  font-weight: bold;
}

.neutral {
  color: rgba(255, 255, 255, 0.8) !important;
}

</style>