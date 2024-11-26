<template>
  <div class="investment-test">
    <h1 class="test-title">투자 성향 테스트</h1>
    <div v-if="loading">로딩 중...</div>
    <div v-else-if="currentQuestion" class="test-container">
      <!-- 진행 상황 표시 -->
      <div class="progress">
        Question {{ currentQuestionNum }} / {{ totalQuestions }}
      </div>

      <!-- 현재 질문 표시 -->
      <div class="question-box">
        <h2>{{ currentQuestion.question_text }}</h2>
      </div>

      <!-- 선택지 -->
      <div class="choices-container">
        <div
          v-for="choice in currentQuestion.choices"
          :key="choice.id"
          class="choice-box"
          :class="{
            selected: answers['question_' + currentQuestion.id] === choice.id,
          }"
          @click="selectAnswer(choice.id)"
        >
          {{ choice.choice_text }}
        </div>
      </div>

      <!-- 이전/다음 버튼 -->
      <div class="navigation-buttons">
        <button
          @click="previousQuestion"
          :disabled="currentQuestionNum === 1"
          class="nav-button"
        >
          이전
        </button>
        <button
          v-if="currentQuestionNum < totalQuestions"
          @click="nextQuestion"
          :disabled="!answers['question_' + currentQuestion.id]"
          class="nav-button"
        >
          다음
        </button>
        <button
          v-else
          @click="submitAnswers"
          :disabled="!answers['question_' + currentQuestion.id]"
          class="nav-button submit-button"
        >
          제출
        </button>
      </div>
    </div>
    <div v-else>질문을 불러오는데 실패했습니다.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const currentQuestion = ref(null);
const currentQuestionNum = ref(1);
const totalQuestions = ref(0);
const answers = ref({});
const loading = ref(true);

const authStore = useAuthStore();
const token = authStore.token;

const fetchQuestion = async (questionNum) => {
  try {
    loading.value = true;
    const response = await axios.get(
      `http://127.0.0.1:8000/investment_style/test/?question=${questionNum}`,
      {
        headers: {
          Authorization: `Token ${authStore.token}`,
        },
      }
    );
    currentQuestion.value = response.data.question;
    currentQuestionNum.value = response.data.current_question;
    totalQuestions.value = response.data.total_questions;
  } catch (error) {
    console.error("질문을 불러오는데 실패했습니다:", error);
  } finally {
    loading.value = false;
  }
};

const nextQuestion = () => {
  if (currentQuestionNum.value < totalQuestions.value) {
    fetchQuestion(currentQuestionNum.value + 1);
  }
};

const previousQuestion = () => {
  if (currentQuestionNum.value > 1) {
    fetchQuestion(currentQuestionNum.value - 1);
  }
};

onMounted(() => {
  fetchQuestion(1);
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

// 변 선택 함수 추가
const selectAnswer = (choiceId) => {
  answers.value["question_" + currentQuestion.value.id] = choiceId;
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap");

body {
  background-color: #0c0f2e;
  color: #ffffff;
  font-family: "Nanum Gothic", sans-serif;
}

.test-title {
  font-family: "Nanum Gothic", sans-serif;
  font-size: 2.2em;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 30px;
  text-align: center;
  letter-spacing: 1px;
  padding: 20px 0;
}

.test-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.progress {
  text-align: center;
  font-size: 1.2em;
  color: #ffffff;
  background-color: rgba(255, 255, 255, 0.1);
  padding: 10px 20px;
  border-radius: 20px;
  margin-bottom: 20px;
  border: 1px solid #ffe81f;
  font-family: "Nanum Gothic", sans-serif;
  font-weight: 400;
}

.question-box {
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 15px;
  padding: 15px;
  margin-bottom: 20px;
  width: 90%;
  max-width: 600px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100px;
}

.question-box h2 {
  margin: 0;
  color: #ffffff;
  text-align: center;
  font-family: "Nanum Gothic", sans-serif;
  font-size: 1.3em;
  font-weight: 700;
  line-height: 1.6;
}

.choices-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 15px;
}

.choice-box {
  background-color: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 10px;
  padding: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 8px;
  font-family: "Nanum Gothic", sans-serif;
  font-size: 1em;
  font-weight: 500;
  width: 90%;
  max-width: 600px;
  min-height: 50px;
}

.choice-box:hover {
  transform: translateY(-2px);
  background-color: rgba(255, 255, 255, 0.2);
}

.choice-box.selected {
  background-color: rgba(255, 238, 31, 0.15);
  font-weight: 650;
  box-shadow: none;
}

.nav-button,
.submit-button {
  background-color: transparent;
  border: 2px solid #ffe81f;
  color: #ffffff;
  padding: 10px 20px;
  margin: 10px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: "Nanum Gothic", sans-serif;
  font-weight: 700;
}

.nav-button:hover,
.submit-button:hover {
  background-color: rgba(255, 238, 31, 0.2);
  box-shadow: 0 0 15px #ffe81f;
}

.navigation-buttons {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .test-title {
    font-size: 2em;
  }

  .choice-box {
    padding: 12px;
  }
}

/* 모든 텍스트 요소에 대한 기본 스타일 */
* {
  font-family: "Nanum Gothic", sans-serif;
}
</style>
