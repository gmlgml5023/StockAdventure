<template>
  <div class="update-form">
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="stock_name">종목명: </label>
        <input 
          type="text" 
          id="stock_name" 
          v-model="formData.stock_name"
          required
        >
      </div>
      <div>
        <label for="transaction_date">거래일자: </label>
        <input 
          type="date" 
          id="transaction_date" 
          v-model="formData.transaction_date"
          required
        >
      </div>
      <div>
        <label for="buysell">거래유형: </label>
        <select 
          id="buysell" 
          v-model="formData.buysell"
          required
        >
          <option value="매수">매수</option>
          <option value="매도">매도</option>
        </select>
      </div>
      <div>
        <label for="quantity">거래수량: </label>
        <input 
          type="number" 
          id="quantity" 
          v-model="formData.quantity"
          required
        >
      </div>
      <div>
        <label for="price">거래가격: </label>
        <input 
          type="number" 
          id="price" 
          v-model="formData.price"
          required
        >
      </div>
      <div>
        <label for="reason">매매이유: </label>
        <textarea 
          id="reason" 
          v-model="formData.reason"
          required
        ></textarea>
      </div>
      <div>
        <label for="feedback">피드백: </label>
        <textarea 
          id="feedback" 
          v-model="formData.feedback"
          required
        ></textarea>
      </div>
      <div class="button-group">
        <button type="submit">제출</button>
        <button type="button" @click="$emit('cancel')">취소</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useJournalStore } from '@/stores/journal'
import { useRouter } from 'vue-router'

const props = defineProps({
  journal: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['update-complete', 'cancel'])
const store = useJournalStore()
const router = useRouter()

const formData = ref({
  stock_name: props.journal.stock_name,
  transaction_date: props.journal.transaction_date,
  buysell: props.journal.buysell,
  quantity: props.journal.quantity,
  price: props.journal.price,
  reason: props.journal.reason,
  feedback: props.journal.feedback
})

const handleSubmit = async () => {
  if (confirm('매매일지를 수정하시겠습니까?')) {
    try {
      await store.updateJournal(props.journal.id, formData.value)
      emit('update-complete')
      
      router.push({ 
        name: 'DetailView', 
        params: { journal_id: props.journal.id }
      }).then(() => {
        alert('매매일지가 수정되었습니다.')
      })
    } catch (error) {
      console.error('수정 실패:', error)
      alert('매매일지 수정에 실패했습니다.')
    }
  }
}
</script>