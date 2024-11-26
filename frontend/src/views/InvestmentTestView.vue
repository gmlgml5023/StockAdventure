<template>
  <div class="investment-test">
    <h1 class="test-title">투자 성향 테스트</h1>
    <div v-if="loading">로딩 중...</div>
    <div v-else-if="currentQuestion" class="test-container">
      <!-- 진행 상황 표시 -->
      <div class="progress-container">
        <div class="progress-bar">
          <div class="stars">
            <span v-for="n in 7" :key="n" class="star" :class="{ 'active': n < currentQuestionNum }">⭐</span>
          </div>
          <div class="rocket" :style="{ left: getRocketPosition(currentQuestionNum) }">🚀</div>
          <div class="progress-fill" :style="{ width: getProgressWidth(currentQuestionNum) }"></div>
        </div>
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

const getRocketPosition = (questionNum) => {
  const positions = [4.3, 18.6, 33.65, 49, 64.3, 79.8, 95.7];
  const position = positions[questionNum - 1];
  
  return `${position}%`;
};

const getProgressWidth = (questionNum) => {
  const positions = [4.3, 18.6, 33.65, 49, 64.3, 79.8, 95.7];
  const position = positions[questionNum - 1];
  
  // 마지막 문항에서는 게이지가 100% 차도록 조정
  if (questionNum === 7) {
    return '100%';
  }
  
  return `${position}%`;
};
</script>

<style scoped>
body {
  background-color: #0c0f2e;
  color: #ffffff;
}

.test-title {
  font-size: 2em;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 20px;
  text-align: center;
  letter-spacing: 1px;
  padding: 15px 0;
}

.test-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.progress-container {
  width: 95%;
  max-width: 650px;
  margin: 20px auto;
}

.progress-bar {
  background: rgba(255, 255, 255, 0.1);
  height: 20px;
  border-radius: 25px;
  border: 2px solid #ffe81f;
  position: relative;
  overflow: visible;
  padding: 0;
  box-sizing: border-box;
}

.progress-fill {
  background: linear-gradient(90deg, #ffe81f 0%, #ffd700 100%);
  height: 100%;
  transition: width 0.5s ease;
  position: absolute;
  top: 0;
  left: 0;
  border-radius: 25px;
  overflow: visible;
}

.rocket {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 20px;
  filter: drop-shadow(0 0 5px rgba(255, 232, 31, 0.7));
  transition: left 0.5s ease;
  z-index: 2;
  margin-left: -10px;
}

.stars {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: calc(100% - 30px);
  display: flex;
  justify-content: space-between;
  pointer-events: none;
  z-index: 1;
  margin: 0 auto;
  left: 15px;
}

.star {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
  width: 20px;
  text-align: center;
}

.star.active {
  color: #ffe81f;
  filter: drop-shadow(0 0 3px rgba(255, 232, 31, 0.7));
  transform: scale(1.2);
}

.question-box {
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 15px;
  padding: 15px;
  margin-bottom: 18px;
  width: 95%;
  max-width: 650px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 95px;
  word-break: keep-all;
  white-space: pre-wrap;
}

.question-box h2 {
  margin: 0;
  color: #ffffff;
  text-align: center;
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
  margin-bottom: 7px;
  width: 95%;
  max-width: 650px;
  min-height: 48px;
  word-break: keep-all;
  white-space: pre-wrap;
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
  padding: 8px 16px;
  margin: 8px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
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
</style>
