<template>
  <div>
  <div class="filter-section">
    <!-- 왼쪽 검색창 -->
    <div class="search-box">
      <input 
        :value="searchQuery"
        @input="updateSearchQuery"
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
    <div class="table-container">
    <div v-if="loading" class="loading-message">
      주식 데이터를 불러오는 중입니다...
    </div>

    <table v-else class="stock-table">
      <thead>
        <tr>
          <th @click="sortBy('stock_id')">
            종목코드
            <span class="sort-arrow">
              {{ getSortArrow('stock_id') }}
            </span>
          </th>
          <th @click="sortBy('stock_name')">
            종목명
            <span class="sort-arrow">
              {{ getSortArrow('stock_name') }}
            </span>
          </th>
          <th @click="sortBy('current_price')">
            현재가
            <span class="sort-arrow">
              {{ getSortArrow('current_price') }}
            </span>
          </th>
          <th @click="sortBy('price_change')">
            등락
            <span class="sort-arrow">
              {{ getSortArrow('price_change') }}
            </span>
          </th>
          <th @click="sortBy('price_change_rate')">
            등락율
            <span class="sort-arrow">
              {{ getSortArrow('price_change_rate') }}
            </span>
          </th>
          <th @click="sortBy('volume')">
            거래량
            <span class="sort-arrow">
              {{ getSortArrow('volume') }}
            </span>
          </th>
          <th @click="sortBy('beta')">
            베타
            <span class="sort-arrow">
              {{ getSortArrow('beta') }}
            </span>
          </th>
          <th @click="sortBy('roa')">
            ROA
            <span class="sort-arrow">
              {{ getSortArrow('roa') }}
            </span>
          </th>
          <th @click="sortBy('roe')">
            ROE
            <span class="sort-arrow">
              {{ getSortArrow('roe') }}
            </span>
          </th>
          <th @click="sortBy('eps')">
            EPS
            <span class="sort-arrow">
              {{ getSortArrow('eps') }}
            </span>
          </th>
          <th @click="sortBy('bps')">
            BPS
            <span class="sort-arrow">
              {{ getSortArrow('bps') }}
            </span>
          </th>
          <th @click="sortBy('per')">
            PER
            <span class="sort-arrow">
              {{ getSortArrow('per') }}
            </span>
          </th>
          <th @click="sortBy('pbr')">
            PBR
            <span class="sort-arrow">
              {{ getSortArrow('pbr') }}
            </span>
          </th>
          <th @click="sortBy('sector')">
            업종
            <span class="sort-arrow">
              {{ getSortArrow('sector') }}
            </span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stock in paginatedStocks" :key="stock.stock_id" class="stock-row">
          <td>{{ stock.stock_id }}</td>
          <td>
            <span @click="goToNaverStock(stock.stock_id)" class="stock-name">
              {{ stock.stock_name }}
              <span class="link-icon">🔗</span>
            </span>  
          </td>
          <td class="number">{{ formatPrice(stock.current_price) }}</td>
          <td class="number" :class="getPriceChangeClass(stock.price_change)">
            {{ formatPriceChange(stock.price_change) }}
          </td>
          <td class="number" :class="getPriceChangeClass(stock.price_change_rate)">
            {{ formatPercent(stock.price_change_rate) }}
          </td>
          <td class="number">{{ formatVolume(stock.volume) }}</td>
          <td class="number">{{ formatDecimal(stock.beta) }}</td>
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
    </div>
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

function goToNaverStock(stockId) {
  window.open(`https://finance.naver.com/item/main.nhn?code=${stockId}`, '_blank');
}

const uniqueSectors = computed(() => {
  const sectors = [...new Set(stocks.value.map(stock => stock.sector))]
  return sectors.filter(sector => sector && sector !== 'Nan').sort()
})

const updateSearchQuery = (event) => {
  searchQuery.value = event.target.value
}

const filteredStocks = computed(() => {

// filteredStocks computed 속성 수정
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
  return sortedStocks.value.slice(startIndex, endIndex)
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

const sortKey = ref('')
const sortOrder = ref('asc')

const sortBy = (key) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

const getSortArrow = (key) => {
  if (sortKey.value !== key) return '↕'
  return sortOrder.value === 'asc' ? '↑' : '↓'
}

const sortedStocks = computed(() => {
  return [...filteredStocks.value].sort((a, b) => {
    let aValue = a[sortKey.value]
    let bValue = b[sortKey.value]

    if (typeof aValue === 'string') {
      aValue = aValue.toLowerCase()
      bValue = bValue.toLowerCase()
    }

    if (aValue < bValue) return sortOrder.value === 'asc' ? -1 : 1
    if (aValue > bValue) return sortOrder.value === 'asc' ? 1 : -1
    return 0
  })
})



watch(selectedSector, () => {
  currentPage.value = 1
})

onMounted(() => {
  fetchStocks()
})
</script>

<style scoped>

.stock-name {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: #f0db37;
  transition: all 0.3s ease;
}

/* 필터 섹션 스타일링 */
.filter-section {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  border-radius: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.search-input {
  width: 300px;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background: rgba(0, 0, 0, 0.2);
  color: rgba(255, 255, 255, 0.5);
  font-size: 16px;
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.sector-select {
  padding: 12px;
  min-width: 200px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background: rgba(0, 0, 0, 0.2);
  color: #f0db37;
  font-size: 16px;
}

.sector-select option {
  background-color: rgba(0, 0, 0, 0.9);
  color: #f0db37;
  padding: 12px;
}

/* 옵션에 마우스를 올렸을 때의 스타일 */
.sector-select option:hover {
  background-color: rgba(240, 219, 55, 0.2);
}

/* 선택된 옵션의 스타일 */
.sector-select option:checked {
  background-color: rgba(240, 219, 55, 0.3);
}

/* 테이블 컨테이너 */
.table-container {
  max-width: 2000px;
  margin: 0 auto;
  height: 70vh;
  overflow-y: auto;
  overflow-x: auto;
  border-radius: 15px;
  /* background: rgba(0, 0, 0, 0.3); */
  background: rgba(152, 149, 125, 0.1);

  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  padding: 10px, 10px, 0px, 10px;
}

/* 테이블 스타일링 */
.stock-table {
  width: 100%;
  min-width: 1500px; /* 테이블 최소 너비 설정 */
  border-collapse: separate;
  border-spacing: 0;
}

.stock-table th {
  position: sticky;
  top: 0;
  z-index: 1;
  padding: 15px;
  background: rgba(0, 0, 0, 1);
  color: #f0db37;
  font-weight: bold;
  text-align: left;
  border-bottom: 2px solid rgba(240, 219, 55, 0.2);
}

.stock-table td {
  padding: 15px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  color: rgba(255, 255, 255, 0.8);
}


/* 각 열의 너비 고정 */
.stock-table th,
.stock-table td {
  white-space: nowrap;
}

.stock-table th:nth-child(1),
.stock-table td:nth-child(1) {
  width: 100px; /* 종목코드 */
}

.stock-table th:nth-child(2),
.stock-table td:nth-child(2) {
  width: 150px; /* 종목명 */
}

.stock-table th:nth-child(3),
.stock-table td:nth-child(3) {
  width: 100px; /* 현재가 */
}

.stock-table th:nth-child(4),
.stock-table td:nth-child(4),
.stock-table th:nth-child(5),
.stock-table td:nth-child(5) {
  width: 80px; /* 등락, 등락율 */
}

.stock-table th:nth-child(6),
.stock-table td:nth-child(6) {
  width: 100px; /* 거래량 */
}

.stock-table th:nth-child(n+7),
.stock-table td:nth-child(n+7) {
  width: 120px; /* 나머지 항목들 */
}

.stock-row {
  transition: all 0.3s ease;
}

.stock-row:hover td {
  background: rgba(240, 219, 55, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.1);
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

/* 페이지네이션 스타일링 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
  gap: 20px;
}

.page-button {
  padding: 12px 24px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background: rgba(0, 0, 0, 0.3);
  color: #f0db37;
  cursor: pointer;
  transition: all 0.3s ease;
}

.page-button:hover:not(:disabled) {
  background: rgba(240, 219, 55, 0.2);
  transform: translateY(-2px);
}

.page-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #f0db37;
  font-size: 16px;
}

.loading-message {
  text-align: center;
  padding: 40px;
  color: #f0db37;
  font-size: 18px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border-radius: 15px;
  margin: 20px 0;
}

/* 스크롤바 스타일링 */
.table-container::-webkit-scrollbar {
  width: 8px;  /* 세로 스크롤바 너비 */
  height: 8px; /* 가로 스크롤바 높이 */
}

.table-container::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
}

.table-container::-webkit-scrollbar-thumb {
  background: rgba(240, 219, 55, 0.3);
  border-radius: 4px;
}

.table-container::-webkit-scrollbar-thumb:hover {
  background: rgba(240, 219, 55, 0.5);
}

.sort-arrow {
  margin-left: 5px;
  color: #f0db37;
  opacity: 0.5;
}

.stock-table th {
  cursor: pointer;
}

.stock-table th:hover .sort-arrow {
  opacity: 1;
}
</style>