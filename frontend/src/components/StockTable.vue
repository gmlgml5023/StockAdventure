// src/components/StockTable.vue
<template>
  <table class="stock-table">
    <thead>
      <tr>
        <th>종목코드</th>
        <th>종목명</th>
        <th>현재가</th>
        <th>등락</th>
        <th>등락율</th>
        <th>거래량</th>
        <th>시가총액</th>
        <th>PER</th>
        <th>PBR</th>
        <th>ROE</th>
        <th>업종</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="stock in stocks" :key="stock.종목코드" class="stock-row">
        <td>{{ stock.종목코드 }}</td>
        <td>{{ stock.종목명 }}</td>
        <td class="number">{{ formatPrice(stock.종가) }}</td>
        <td class="number" :class="getPriceChangeClass(stock.등락)">
          {{ formatChange(stock.등락) }}
        </td>
        <td class="number" :class="getPriceChangeClass(stock.등락율)">
          {{ formatPercent(stock.등락율) }}
        </td>
        <td class="number">{{ stock.거래량 }}</td>
        <td class="number">{{ stock.시가총액 }}</td>
        <td class="number">{{ formatRatio(stock.PER) }}</td>
        <td class="number">{{ formatRatio(stock.PBR) }}</td>
        <td class="number">{{ formatPercent(stock.ROE) }}</td>
        <td>{{ stock.업종 }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps({
  stocks: {
    type: Array,
    required: true
  }
})

// 가격 포맷팅 (천 단위 구분)
const formatPrice = (value) => {
  if (!value || value === 'Nan') return '-'
  return new Intl.NumberFormat('ko-KR').format(value)
}

// 등락 포맷팅
const formatChange = (value) => {
  if (!value || value === 'Nan') return '-'
  return (value > 0 ? '+' : '') + new Intl.NumberFormat('ko-KR').format(value)
}

// 퍼센트 포맷팅
const formatPercent = (value) => {
  if (!value || value === 'Nan') return '-'
  return value.toFixed(2) + '%'
}

// // 거래량 포맷팅 (K, M 단위)
// const formatVolume = (value) => {
//   if (!value || value === 'Nan') return '-'
//   if (value >= 1000000) {
//     return (value / 1000000).toFixed(1) + 'M'
//   }
//   if (value >= 1000) {
//     return (value / 1000).toFixed(1) + 'K'
//   }
//   return value.toString()
// }

// // 시가총액 포맷팅 (억, 조 단위)
// const formatMarketCap = (value) => {
//   if (!value || value === 'Nan') return '-'
//   if (value >= 1000000000000) {
//     return (value / 1000000000000).toFixed(2) + '조'
//   }
//   return (value / 100000000).toFixed(0) + '억'
// }

// 비율 포맷팅
const formatRatio = (value) => {
  if (!value || value === 'Nan') return '-'
  return value.toFixed(2)
}

// 등락에 따른 색상 클래스
const getPriceChangeClass = (value) => {
  if (!value || value === 0) return 'neutral'
  return value > 0 ? 'up' : 'down'
}
</script>

<style scoped>
.stock-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  font-size: 14px;
}

.stock-table th,
.stock-table td {
  padding: 12px;
  border: 1px solid #ddd;
  text-align: left;
}

.stock-table th {
  background-color: #f5f5f5;
  font-weight: bold;
  position: sticky;
  top: 0;
}

.stock-table .number {
  text-align: right;
  /* font-family: 'Courier New', monospace; */
}

.stock-row:hover {
  background-color: #f8f9fa;
  cursor: pointer;
}

/* 등락 색상 */
.up { 
  color: #d24f45; 
  font-weight: bold;
}

.down { 
  color: #1261c4; 
  font-weight: bold;
}

.neutral { 
  color: #000; 
}
</style>