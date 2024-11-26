<template>
  <div class="journal-container">
    <h1 class="journal-title">매매일지 작성</h1>
    <form @submit.prevent="handleSubmit" class="journal-form">
      <div class="form-group">
        <label for="stock_name">종목명</label>
        <input 
          type="text" 
          id="stock_name" 
          v-model.trim="formData.stock_name" 
          required
          class="form-input"
          placeholder="종목명을 입력하세요"
        >
      </div>

      <div class="form-group">
        <label for="transaction_date">거래일자</label>
        <input 
          type="date" 
          id="transaction_date" 
          v-model="formData.transaction_date" 
          required
          class="form-input"
        >
      </div>

      <div class="form-group">
        <label for="buysell">거래유형</label>
        <select 
          id="buysell" 
          v-model="formData.buysell" 
          required
          class="form-input"
        >
          <option value="매수">매수</option>
          <option value="매도">매도</option>
        </select>
      </div>

      <div class="form-group">
        <label for="quantity">거래수량</label>
        <input 
          type="number" 
          id="quantity" 
          v-model.number="formData.quantity" 
          required
          class="form-input"
          placeholder="수량을 입력하세요"
        >
      </div>

      <div class="form-group">
        <label for="price">거래가격</label>
        <input 
          type="number" 
          id="price" 
          v-model.number="formData.price" 
          required
          class="form-input"
          placeholder="가격을 입력하세요"
        >
      </div>

      <div class="form-group">
        <label for="reason">매매이유</label>
        <textarea 
          id="reason" 
          v-model.trim="formData.reason" 
          required
          class="form-textarea"
          placeholder="매매 이유를 작성해주세요"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="feedback">피드백</label>
        <textarea 
          id="feedback" 
          v-model.trim="formData.feedback" 
          required
          class="form-textarea"
          placeholder="매매에 대한 피드백을 작성해주세요"
        ></textarea>
      </div>

      <button type="submit" class="submit-button">
        <span class="button-text">제출하기</span>
        <span class="star-icon">📝</span>
      </button>
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

<style scoped>
.journal-container {
  max-width: 600px;
  margin: auto;
  padding: 30px;
  border-radius: 15px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 0 32px rgba(240, 219, 55, 0.05);
}

.journal-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 28px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.form-group {
  margin-bottom: 20px;
}

label {
  color: #f0db37;
  margin-bottom: 8px;
  display: block;
  font-weight: 500;
  text-shadow: 0 0 8px rgba(240, 219, 55, 0.4);
}

.form-input, .form-textarea {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background-color: rgba(0, 0, 0, 0.8);
  color: rgba(255, 255, 255, 0.5);;
  font-size: 16px;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.form-textarea {
  min-height: 100px;
  resize: vertical;
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: rgba(255, 255, 255, 0.5); /* 흰색과 회색의 중간 톤으로 변경 */
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #f0db37;
  box-shadow: 0 0 15px rgba(240, 219, 55, 0.2);
  background: rgba(0, 0, 0, 0.3);
}

.submit-button {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: none;
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 0.9), 
    rgba(255, 209, 4, 0.9)
  );
  color: #000;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.submit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 1), 
    rgba(255, 209, 4, 1)
  );
}

.star-icon {
  font-size: 18px;
}

select.form-input {
  appearance: none;
  background-image: linear-gradient(45deg, transparent 50%, #f0db37 50%),
                    linear-gradient(135deg, #f0db37 50%, transparent 50%);
  background-position: 
    calc(100% - 20px) calc(1em + 2px),
    calc(100% - 15px) calc(1em + 2px);
  background-size: 
    5px 5px,
    5px 5px;
  background-repeat: no-repeat;
}

input[type="date"].form-input {
  color-scheme: dark;
}
</style>