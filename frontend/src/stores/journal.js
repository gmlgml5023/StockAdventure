import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAuthStore } from './auth'

export const useJournalStore = defineStore('journal', () => {
  const journals = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  // const token = ref(null)

  const authStore = useAuthStore()

  const getJournals = async function () {
    if (!authStore.token) {
      console.error('인증 토큰이 없습니다.')
      return
    }
    try {
      const response = await axios.get(`${API_URL}/journals/`, {
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      })
      journals.value = response.data
      console.log('Loaded journals:', journals.value); // 디버깅을 위한 로그
    } catch (error) {
      console.error('매매일지 로딩 실패:', error)
      if (error.response && error.response.status === 401) {
        console.error('인증 토큰이 만료되었거나 유효하지 않습니다.')
        // 여기에 로그아웃 또는 토큰 갱신 로직을 추가할 수 있습니다.
      }
    }
  }

  const updateJournal = async function (journalId, updatedData) {
    if (!authStore.token) {
      console.error('인증 토큰이 없습니다.')
      return
    }
    try {
      return await axios.put(`${API_URL}/journals/${journalId}/`, updatedData, {
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      })
    } catch (error) {
      console.error('매매일지 수정 실패:', error)
      throw error
    }
  }

  const deleteJournal = async function (journalId) {
    if (!authStore.token) {
      console.error('인증 토큰이 없습니다.')
      return
    }
    try {
      return await axios.delete(`${API_URL}/journals/${journalId}/`, {
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      })
    } catch (error) {
      console.error('매매일지 삭제 실패:', error)
      throw error
    }
  }

  const userJournals = computed(() => {
    console.log('All journals:', journals.value);
    console.log('Current user ID:', authStore.user?.id);
    // 임시로 모든 저널 반환
    return journals.value;
    // return journals.value.filter(journal => journal.user && journal.user === authStore.user.id)
  })

  return { journals, API_URL, getJournals, updateJournal, deleteJournal, userJournals }
}, { persist: true })
  // DRF로 전체 매매일지 요청을 보내고 응답을 받아 journals에 저장하는 함수
  // const getJournals = function () {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/journals/`,
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //     }
  //   })
  //     .then((res) => {
  //       journals.value = res.data
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }
  
  // 매매일지 수정 함수
//   const updateJournal = function (journalId, updatedData) {
//     return axios({
//       method: 'put',
//       url: `${API_URL}/journals/${journalId}/`,
//       data: updatedData,
//       headers: {
//         Authorization: `Token ${token.value}` // 인증 토큰 추가
//       }
//     })
//   }

//   // 매매일지 삭제 함수
//   const deleteJournal = function (journalId) {
//     return axios({
//       method: 'delete',
//       url: `${API_URL}/journals/${journalId}/`,
//       headers: {
//         Authorization: `Token ${token.value}` // 인증 토큰 추가
//       }
//     })
//   }
//   // 현재 사용자 ID를 가져오기 위한 인증 스토어
//   const authStore = useAuthStore()

//   // 현재 사용자에 해당하는 매매일지만 필터링하는 getter
//   const userJournals = computed(() => {
//     return journals.value.filter(journal => journal.user && journal.user.id === authStore.user.id)
//   })

//   return { journals, API_URL, getJournals, updateJournal, deleteJournal, token, userJournals }
// }, { persist: true })