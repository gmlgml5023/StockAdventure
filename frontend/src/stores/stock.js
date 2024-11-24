import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useStockStore = defineStore('stock', () => {
  const stocks = ref([])
  const isUpdating = ref(false)
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

  // 주식 데이터 업데이트 요청
  const updateStocks = function () {
    isUpdating.value = true
    axios({
      method: 'post',
      url: `${API_URL}/stocks/update/`,
    })
      .then(() => {
        getStocks()
        isUpdating.value = false
      })
      .catch((err) => {
        console.log(err)
        isUpdating.value = false
      })
  }

  return { stocks, isUpdating, getStocks, updateStocks }
})