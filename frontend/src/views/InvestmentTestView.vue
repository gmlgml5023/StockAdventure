<template>
  <div class="investment-test">
    <h1>투자 성향 검사</h1>
    <div v-if="loading">로딩 중...</div>
    <div v-else-if="questions.length">
      <div v-for="question in questions" :key="question.id" class="question">
        <h2>{{ question.question_text }}</h2>
        <div v-for="choice in question.choices" :key="choice.id" class="choice">
          <input
            type="radio"
            :id="'choice' + choice.id"
            :value="choice.id"
            v-model="answers['question_' + question.id]"
          />
          <label :for="'choice' + choice.id">{{ choice.choice_text }}</label>
        </div>
      </div>
      <button @click="submitAnswers" :disabled="!isFormValid">제출</button>
    </div>
    <div v-else>질문을 불러오는데 실패했습니다.</div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const questions = ref([]);
const answers = ref({});
const loading = ref(true);

const authStore = useAuthStore();
const token = authStore.token;

const isFormValid = computed(() => {
  return questions.value.every((q) => answers.value["question_" + q.id]);
});

onMounted(async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/investment_style/test/",
      {
        headers: {
          Authorization: `Token ${authStore.token}`,
        },
      }
    );
    questions.value = response.data;
  } catch (error) {
    console.error("질문을 불러오는데 실패했습니다:", error);
  } finally {
    loading.value = false;
  }
});

const submitAnswers = async () => {
  try {
    console.log("Submitting answers:", answers.value);
    const response = await axios.post(
      "http://127.0.0.1:8000/investment_style/test/",
      answers.value,
      {
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "application/json",
        },
      }
    );
    console.log("Response:", response.data);
    router.push({
      name: "investment-result",
      query: { investment_style_id: response.data.investment_style_id },
    });
  } catch (error) {
    console.error("답변 제출에 실패했습니다:", error);
  }
};
</script>
