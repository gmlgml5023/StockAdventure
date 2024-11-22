import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  // const token = ref(null)

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 게시글 수정 함수
  const updateArticle = function (articleId, updatedData) {
    return axios({
      method: 'put',
      url: `${API_URL}/articles/${articleId}/`,
      data: updatedData
    })
  }

  // 게시글 삭제 함수
  const deleteArticle = function (articleId) {
    return axios({
      method: 'delete',
      url: `${API_URL}/articles/${articleId}/`
    })
  }

  return { articles, API_URL, getArticles, updateArticle, deleteArticle }
  // return { articles, API_URL, getArticles, token }
}, { persist: true })

