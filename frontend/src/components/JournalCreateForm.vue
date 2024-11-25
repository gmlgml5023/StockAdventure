<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="stock_name">종목명: </label>
        <input type="text" id="stock_name" v-model.trim="formData.stock_name" required>
      </div>
      <div>
        <label for="transaction_date">거래일자: </label>
        <input type="date" id="transaction_date" v-model="formData.transaction_date" required>
      </div>
      <div>
        <label for="buysell">거래유형: </label>
        <select id="buysell" v-model="formData.buysell" required>
          <option value="매수">매수</option>
          <option value="매도">매도</option>
        </select>
      </div>
      <div>
        <label for="quantity">거래수량: </label>
        <input type="number" id="quantity" v-model.number="formData.quantity" required>
      </div>
      <div>
        <label for="price">거래가격: </label>
        <input type="number" id="price" v-model.number="formData.price" required>
      </div>
      <div>
        <label for="reason">매매이유: </label>
        <textarea id="reason" v-model.trim="formData.reason" required></textarea>
      </div>
      <div>
        <label for="feedback">피드백: </label>
        <textarea id="feedback" v-model.trim="formData.feedback" required></textarea>
      </div>
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useJournalStore } from '@/stores/journal'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const emit = defineEmits(['create-complete'])
const store = useJournalStore()
const router = useRouter()
const authStore = useAuthStore()

const formData = ref({
  stock_name: '',
  transaction_date: '',
  buysell: '매수',
  quantity: 0,
  price: 0,
  reason: '',
  feedback: ''
})

const handleSubmit = async () => {
  try {
    await axios({
      method: 'post',
      url: `${store.API_URL}/journals/`,
      data: formData.value,
      headers: {
        'Authorization': `Token ${authStore.token}`
      }
    })
    emit('create-complete')
    router.push({ name: 'JournalView' })
  } catch (err) {
    console.error('매매일지 작성 실패:', err)
  }
}
</script>