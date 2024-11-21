import { defineStore } from 'pinia'
import axios from '@/plugins/axios'

export const useArticleStore = defineStore('article', {
  state: () => ({
    articles: [],
    currentArticle: null,
    loading: false,
    error: null
  }),
  
  actions: {
    async fetchArticles() {
      this.loading = true
      try {
        const response = await axios.get('articles/')
        this.articles = response.data
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },
    
    async fetchArticle(id) {
      this.loading = true
      try {
        const response = await axios.get(`articles/${id}/`)
        this.currentArticle = response.data
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },

    async createArticle(articleData) {
      try {
        const response = await axios.post('articles/', articleData)
        this.articles.push(response.data)
        return response.data
      } catch (error) {
        this.error = error.message
        throw error
      }
    },

    async updateArticle(id, articleData) {
      try {
        const response = await axios.put(`articles/${id}/`, articleData)
        const index = this.articles.findIndex(article => article.id === id)
        if (index !== -1) {
          this.articles[index] = response.data
        }
        return response.data
      } catch (error) {
        this.error = error.message
        throw error
      }
    }
  }
})