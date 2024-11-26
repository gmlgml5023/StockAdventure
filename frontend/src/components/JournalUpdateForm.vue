<template>
  <div class="update-form">
    <h2 class="form-title">매매일지 수정하기</h2>
    <form @submit.prevent="handleSubmit" class="journal-form">
      <div class="form-group">
        <label for="stock_name">종목명</label>
        <input
          type="text"
          id="stock_name"
          v-model="formData.stock_name"
          required
          class="form-input"
          placeholder="종목명을 입력하세요"
        />
      </div>

      <div class="form-group">
        <label for="transaction_date">거래일자</label>
        <input
          type="date"
          id="transaction_date"
          v-model="formData.transaction_date"
          required
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label for="buysell">거래유형</label>
        <select id="buysell" v-model="formData.buysell" required class="form-input">
          <option value="매수">매수</option>
          <option value="매도">매도</option>
        </select>
      </div>

      <div class="form-group">
        <label for="quantity">거래수량</label>
        <input
          type="number"
          id="quantity"
          v-model="formData.quantity"
          required
          class="form-input"
          placeholder="수량을 입력하세요"
        />
      </div>

      <div class="form-group">
        <label for="price">거래가격</label>
        <input 
          type="number" 
          id="price" 
          v-model="formData.price" 
          required 
          class="form-input"
          placeholder="가격을 입력하세요"
        />
      </div>

      <div class="form-group">
        <label for="reason">매매이유</label>
        <textarea 
          id="reason" 
          v-model="formData.reason" 
          required
          class="form-textarea"
          placeholder="매매 이유를 작성해주세요"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="feedback">피드백</label>
        <textarea 
          id="feedback" 
          v-model="formData.feedback" 
          required
          class="form-textarea"
          placeholder="매매에 대한 피드백을 작성해주세요"
        ></textarea>
      </div>

      <div class="button-group">
        <button type="submit" class="submit-button">
          <span class="button-text">수정완료</span>
          <span class="star-icon">💫</span>
        </button>
        <button type="button" @click="$emit('cancel')" class="cancel-button">
          <span class="button-text">취소</span>
          <span class="star-icon">✖</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useJournalStore } from "@/stores/journal";
import { useRouter } from "vue-router";

const props = defineProps({
  journal: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["update-complete", "cancel"]);
const store = useJournalStore();
const router = useRouter();

const formData = ref({
  stock_name: props.journal.stock_name,
  transaction_date: props.journal.transaction_date,
  buysell: props.journal.buysell,
  quantity: props.journal.quantity,
  price: props.journal.price,
  reason: props.journal.reason,
  feedback: props.journal.feedback,
});

const handleSubmit = async () => {
  if (confirm("매매일지를 수정하시겠습니까?")) {
    try {
      await store.updateJournal(props.journal.id, formData.value);
      emit("update-complete");

      router
        .push({
          name: "JournalDetailView",
          params: { journal_id: props.journal.id },
        })
        .then(() => {
          alert("매매일지가 수정되었습니다.");
        });
    } catch (error) {
      console.error("수정 실패:", error);
      alert("매매일지 수정에 실패했습니다.");
    }
  }
};
</script>

<style scoped>
.update-form {
  max-width: 800px;
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

.form-title {
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
  background: rgba(0, 0, 0, 0.2);
  color: #f0db37;
  font-size: 16px;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #f0db37;
  box-shadow: 0 0 15px rgba(240, 219, 55, 0.2);
  background: rgba(0, 0, 0, 0.3);
}

.button-group {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.submit-button, .cancel-button {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: none;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.submit-button {
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 0.9), 
    rgba(255, 209, 4, 0.9)
  );
  color: #000;
}

.cancel-button {
  background: rgba(255, 255, 255, 0.1);
  color: #f0db37;
  border: 1px solid rgba(240, 219, 55, 0.4);
}

.submit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}

.cancel-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
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