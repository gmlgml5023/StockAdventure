import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useJournalStore = defineStore('journal', () => {
  const journals = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  // const token = ref(null)

  // DRF로 전체 매매일지 요청을 보내고 응답을 받아 journals에 저장하는 함수
  const getJournals = function () {
    axios({
      method: 'get',
      url: `${API_URL}/journals/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) => {
        journals.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 매매일지 수정 함수
  const updateJournal = function (journalId, updatedData) {
    return axios({
      method: 'put',
      url: `${API_URL}/journals/${journalId}/`,
      data: updatedData
    })
  }

  // 매매일지 삭제 함수
  const deleteJournal = function (journalId) {
    return axios({
      method: 'delete',
      url: `${API_URL}/journals/${journalId}/`
    })
  }

  return { journals, API_URL, getJournals, updateJournal, deleteJournal }
  // return { journals, API_URL, getJournals, token }
}, { persist: true })