// src/stores/stock.js
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useStockStore = defineStore('stock', () => {
  const stocks = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 전체 주식 데이터 요청
  const getStocks = function () {
    axios({
      method: 'get',
      url: `${API_URL}/stocks/`,
    })
      .then((res) => {
        stocks.value = res.data.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { stocks, getStocks }
})