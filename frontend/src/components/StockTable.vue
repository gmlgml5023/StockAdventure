<template>
  <div>
  <div class="filter-section">
    <!-- 왼쪽 검색창 -->
    <div class="search-box">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="종목명 검색..." 
        class="search-input"
      >
    </div>
    
    <!-- 오른쪽 업종 필터 -->
    <div class="sector-box">
      <select v-model="selectedSector" class="sector-select">
        <option value="">전체 업종</option>
        <option v-for="sector in uniqueSectors" :key="sector" :value="sector">
          {{ sector }}
        </option>
      </select>
    </div>
  </div>

    <div v-if="loading" class="loading-message">
      주식 데이터를 불러오는 중입니다...
    </div>

    <table v-else class="stock-table">
      <thead>
        <tr>
          <th>종목코드</th>
          <th>종목명</th>
          <th>현재가</th>
          <th>등락</th>
          <th>등락율</th>
          <th>거래량</th>
          <th>거래대금</th>
          <th>시가총액</th>
          <th>발행주식수</th>
          <th>베타</th>
          <th>부채비율</th>
          <th>유보율</th>
          <th>매출액증가율</th>
          <th>EPS증가율</th>
          <th>ROA</th>
          <th>ROE</th>
          <th>EPS</th>
          <th>BPS</th>
          <th>PER</th>
          <th>PBR</th>
          <th>업종</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stock in paginatedStocks" :key="stock.stock_id" class="stock-row">
          <td>{{ stock.stock_id }}</td>
          <td>{{ stock.stock_name }}</td>
          <td class="number">{{ formatPrice(stock.current_price) }}</td>
          <td class="number" :class="getPriceChangeClass(stock.price_change)">
            {{ formatPriceChange(stock.price_change) }}
          </td>
          <td class="number" :class="getPriceChangeClass(stock.price_change_rate)">
            {{ formatPercent(stock.price_change_rate) }}
          </td>
          <td class="number">{{ formatVolume(stock.volume) }}</td>
          <td class="number">{{ formatCapital(stock.trading_value) }}</td>
          <td class="number">{{ formatCapital(stock.market_cap) }}</td>
          <td class="number">{{ formatVolume(stock.issued_shares) }}</td>
          <td class="number">{{ formatDecimal(stock.beta) }}</td>
          <td class="number">{{ formatPercent(stock.debt_ratio) }}</td>
          <td class="number">{{ formatPercent(stock.retention_ratio) }}</td>
          <td class="number">{{ formatPercent(stock.revenue_growth_rate) }}</td>
          <td class="number">{{ stock.eps_growth_rate }}</td>
          <td class="number">{{ formatPercent(stock.roa) }}</td>
          <td class="number">{{ formatPercent(stock.roe) }}</td>
          <td class="number">{{ formatDecimal(stock.eps) }}</td>
          <td class="number">{{ formatDecimal(stock.bps) }}</td>
          <td class="number">{{ formatDecimal(stock.per) }}</td>
          <td class="number">{{ formatDecimal(stock.pbr) }}</td>
          <td>{{ stock.sector }}</td>
        </tr>
      </tbody>
    </table>

    <div class="pagination">
      <button 
        :disabled="currentPage === 1" 
        @click="currentPage--"
        class="page-button"
      >
        이전
      </button>
      <span class="page-info">
        {{ currentPage }} / {{ totalPages }} 페이지
      </span>
      <button 
        :disabled="currentPage === totalPages" 
        @click="currentPage++"
        class="page-button"
      >
        다음
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'

const stocks = ref([])
const loading = ref(true)
const selectedSector = ref('')
const currentPage = ref(1)
const itemsPerPage = ref(20)
const searchQuery = ref('')  // 검색어 상태 추가

const uniqueSectors = computed(() => {
  const sectors = [...new Set(stocks.value.map(stock => stock.sector))]
  return sectors.filter(sector => sector && sector !== 'Nan').sort()
})

// filteredStocks computed 속성 수정
const filteredStocks = computed(() => {
  let filtered = stocks.value

  // 검색어로 필터링
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(stock => 
      stock.stock_name.toLowerCase().includes(query) || 
      stock.stock_id.includes(query)
    )
  }

  // 업종으로 필터링
  if (selectedSector.value) {
    filtered = filtered.filter(stock => stock.sector === selectedSector.value)
  }

  // Nan 업종 제외
  return filtered.filter(stock => stock.sector && stock.sector !== 'Nan')
})

// 검색어 변경 시 첫 페이지로 이동
watch(searchQuery, () => {
  currentPage.value = 1
})

const paginatedStocks = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage.value
  const endIndex = startIndex + itemsPerPage.value
  return filteredStocks.value.slice(startIndex, endIndex)
})

const totalPages = computed(() => {
  return Math.ceil(filteredStocks.value.length / itemsPerPage.value)
})

const fetchStocks = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/stocks/')
    stocks.value = response.data.data
  } catch (error) {
    console.error('Error fetching stocks:', error)
  } finally {
    loading.value = false
  }
}

const formatPercent = (value) => {
  if (!value) return '-'
  return value.toFixed(2) + '%'
}

const formatDecimal = (value) => {
  if (!value) return '-'
  return value.toFixed(2)
}

const formatPrice = (value) => {
  if (!value) return '-'
  return new Intl.NumberFormat('ko-KR').format(value)
}

const formatPriceChange = (change) => {
  if (!change) return '-'
  return (change > 0 ? '+' : '') + new Intl.NumberFormat('ko-KR').format(change)
}

const formatVolume = (value) => {
  if (!value) return '-'
  if (value >= 1000000) return (value / 1000000).toFixed(1) + 'M'
  if (value >= 1000) return (value / 1000).toFixed(0) + 'K'
  return value.toString()
}

const formatCapital = (value) => {
  if (!value || value === 'Nan') return '-'
  if (value >= 1000000000000) {
    return (value / 1000000000000).toFixed(2) + '조'
  }
  return (value / 100000000).toFixed(0) + '억'
}

const getPriceChangeClass = (value) => {
  if (!value || value === 0) return 'neutral'
  return value > 0 ? 'up' : 'down'
}

watch(selectedSector, () => {
  currentPage.value = 1
})

onMounted(() => {
  fetchStocks()
})
</script>

<style scoped>
/* 필터 섹션 스타일링 */
.filter-section {
  display: flex;
  justify-content: space-between;  /* 요소들을 양끝으로 분산 */
  align-items: center;
  margin: 20px 0;
  padding: 0 20px;
  gap: 20px;  /* 요소들 사이 간격 */
}

.search-box {
  width: 300px;  /* 검색창 너비 고정 */
}

.search-input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.sector-select {
  padding: 8px 12px;
  min-width: 200px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

/* 테이블 스타일링 */
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
  z-index: 1;
}

.stock-table .number {
  text-align: right;
}

.stock-row:hover {
  background-color: #f8f9fa;
}

/* 상태 메시지 스타일링 */
.loading-message {
  text-align: center;
  padding: 40px;
  color: #666;
  font-size: 16px;
}

/* 가격 변동 색상 */
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

/* 페이지네이션 스타일링 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
  gap: 20px;
}

.page-button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
  cursor: pointer;
}

.page-button:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.page-button:hover:not(:disabled) {
  background-color: #f8f9fa;
}

.page-info {
  font-size: 14px;
  color: #666;
}
</style>