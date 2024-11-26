<template>
  <div class="investment-result">
    <div class="result-container">
      <h1 class="test-title">투자 성향 검사 결과</h1>

      <div class="result-box safe" v-if="investmentStyle === 1">
        <div class="character-icon">
          <img
            src="@/../../backend/media/images/character_1.png"
            alt="안정형 캐릭터"
          />
        </div>
        <h2 class="sub-title">안정적인 미래를 꿈꾸는 투자자</h2>
        <h3 class="type-title">안정형 투자자</h3>
        <div class="content-box">
          <p>
            안정형 투자자는 자산의 안전성과 꾸준한 수익을 중시하는
            투자자입니다.<br />
            변동성이 적은 투자 상품에 집중하며,<br />
            손실을 최소화하고 장기적인 안정성을 추구합니다.
          </p>
          <ul>
            <li>
              위험 회피 성향: 손실에 대한 두려움이 크고, 변동성이 낮은 자산을
              선호합니다.
            </li>
            <li>
              장기 투자: 단기적인 시장 변동에 영향을 받지 않고 장기적인 관점에서
              투자합니다.
            </li>
            <li>
              안정적인 배당 수익: 배당금이 안정적인 기업에 투자하며, 기업의 재무
              건전성을 중요시합니다.
            </li>
            <li>
              투자 전략: 기업의 재무 상태, 낮은 부채 비율, PER, PBR 지표 등을
              고려하여 주식을 선택합니다.
            </li>
          </ul>
        </div>

        <div class="recommendation-section">
          <p class="recommendation-text">
            <span class="user-highlight">{{
              profile_username || nickname || "투자자"
            }}</span
            >님의 투자 성향에 맞는 종목을 추천해 드릴게요!
          </p>
          <RouterLink to="/" class="recommendation-button">
            <span>추천 종목 보러 가기</span>
          </RouterLink>
        </div>
      </div>

      <div class="result-box neutral" v-else-if="investmentStyle === 2">
        <div class="character-icon">
          <img
            src="@/../../backend/media/images/character_2.png"
            alt="위험중립형 캐릭터"
          />
        </div>
        <h2 class="sub-title">안정성과 수익성의 균형을 찾는 투자자</h2>
        <h3 class="type-title">위험중립형 투자자</h3>
        <div class="content-box">
          <p>
            위험중립형 투자자는 안정성과 수익을 모두 중요하게 생각합니다.<br />
            리스크를 분산시키면서도 안정적인 수익을 추구하고,<br />
            시장 상황에 유연하게 대응합니다.
          </p>
          <ul>
            <li>
              균형 잡힌 포트폴리오: 주식과 채권을 혼합하여 포트폴리오를 구성하고
              리스크를 분산시킵니다.
            </li>
            <li>
              시장 변화에 대한 적응력: 시장 상황에 따라 투자 전략을 유연하게
              조정합니다.
            </li>
            <li>
              성장 가능성 탐색: PER이 업종 평균보다 낮은 주식을 찾아 투자합니다.
            </li>
            <li>
              중장기 투자 목표: 장기적인 안정적인 수익을 목표로 중장기적인
              성장을 중시합니다.
            </li>
          </ul>
        </div>

        <div class="recommendation-section">
          <p class="recommendation-text">
            <span class="user-highlight">{{
              profile_username || nickname || "투자자"
            }}</span
            >님의 투자 성향에 맞는 종목을 추천해 드릴게요!
          </p>
          <RouterLink to="/" class="recommendation-button">
            <span>추천 종목 보러 가기</span>
          </RouterLink>
        </div>
      </div>

      <div class="result-box aggressive" v-else-if="investmentStyle === 3">
        <div class="character-icon">
          <img
            src="@/../../backend/media/images/character_3.png"
            alt="공격투자형 캐릭터"
          />
        </div>
        <h2 class="sub-title">높은 수익을 위한 도전을 즐기는 투자자</h2>
        <h3 class="type-title">공격투자형 투자자</h3>
        <div class="content-box">
          <p>
            공격투자형 투자자는 높은 수익을 목표로 하며, 그에 따른 리스크를
            감수할 준비가 되어 있습니다.<br />
            빠르게 변동하는 시장에서 적극적인 투자 전략을 구사합니다.
          </p>
          <ul>
            <li>
              높은 위험 감수: 손실을 감수하고라도 높은 수익을 추구하며, 변동성이
              큰 주식에 투자합니다.
            </li>
            <li>
              단기 거래 선호: 단기적인 가격 변화에 빠르게 반응하며, 자주 매매를
              시도합니다.
            </li>
            <li>
              성장주 선호: 혁신적인 기술을 가진 기업이나 신흥 시장의 주식에
              집중합니다.
            </li>
            <li>
              정보 분석 능력: 최신 정보를 분석하여 빠르게 변하는 시장에
              대응합니다.
            </li>
          </ul>
        </div>

        <div class="recommendation-section">
          <p class="recommendation-text">
            <span class="user-highlight">{{
              profile_username || nickname || "투자자"
            }}</span
            >님의 투자 성향에 맞는 종목을 추천해 드릴게요!
          </p>
          <RouterLink to="/" class="recommendation-button">
            <span>추천 종목 보러 가기</span>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const route = useRoute();
const authStore = useAuthStore();
const token = authStore.token;
const profile_username = ref("");
const nickname = ref("");
const investmentStyle = ref(null);

const fetchUserProfile = async () => {
  try {
    const username = authStore.username;
    const response = await axios.get(
      `http://127.0.0.1:8000/accounts/${username}/`,
      {
        headers: { Authorization: `Token ${token}` },
      }
    );
    profile_username.value = response.data.username;
    nickname.value = response.data.nickname;
    investmentStyle.value = parseInt(route.query.investment_style_id);
  } catch (error) {
    console.error("프로필 로딩 실패:", error);
  }
};

onMounted(() => {
  fetchUserProfile();
});
</script>

<style scoped>
.investment-result {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.result-container {
  max-width: 900px;
  width: 100%;
  z-index: 1;
  padding-top: 1rem;
}

.test-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 32px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
  margin-top: 20px;
}

@media (max-width: 768px) {
  .test-title {
    font-size: 2em;
    margin-top: 15px;
  }
}

.result-box {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2.5rem;
  margin: 2rem 0;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0px);
  }
}

.character-icon {
  text-align: center;
  margin-bottom: 1.5rem;
  animation: float 6s ease-in-out infinite;
}

.character-icon img {
  width: 150px;
  height: 150px;
  object-fit: contain;
  filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.3));
}

.sub-title {
  color: #fff;
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-align: center;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

.type-title {
  color: #7eb6ff;
  font-size: 1.5rem;
  font-weight: 500;
  margin-bottom: 2rem;
  text-align: center;
  text-shadow: 0 0 10px rgba(126, 182, 255, 0.5);
}

.content-box {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 15px;
  padding: 1.5rem;
  margin-top: 1.5rem;
}

p {
  color: #fff;
  line-height: 2;
  margin-bottom: 1.5rem;
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 1.5rem 0;
  text-align: center;
}

li {
  color: #fff;
  margin: 1rem 0;
  padding-left: 0;
  position: relative;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
}

li::before {
  content: "★";
  color: inherit;
  position: static;
  font-weight: bold;
}

@media (max-width: 768px) {
  .result-container {
    padding: 1rem;
  }

  .sub-title {
    font-size: 1.5rem;
  }

  .type-title {
    font-size: 1.2rem;
  }
}

.result-box.safe {
  background: rgba(41, 98, 255, 0.1);
  border: 1px solid rgba(41, 98, 255, 0.2);
  box-shadow: 0 0 20px rgba(41, 98, 255, 0.2);
}

.result-box.safe .type-title {
  color: #4b83ff;
  text-shadow: 0 0 10px rgba(41, 98, 255, 0.5);
}

.result-box.safe li::before {
  color: #4b83ff;
}

.result-box.neutral {
  background: rgba(255, 196, 0, 0.1);
  border: 1px solid rgba(255, 196, 0, 0.2);
  box-shadow: 0 0 20px rgba(255, 196, 0, 0.2);
}

.result-box.neutral .type-title {
  color: #ffd700;
  text-shadow: 0 0 10px rgba(255, 196, 0, 0.5);
}

.result-box.neutral li::before {
  color: #ffd700;
}

.result-box.aggressive {
  background: rgba(147, 51, 234, 0.1);
  border: 1px solid rgba(147, 51, 234, 0.2);
  box-shadow: 0 0 20px rgba(147, 51, 234, 0.2);
}

.result-box.aggressive .type-title {
  color: #b388ff;
  text-shadow: 0 0 10px rgba(147, 51, 234, 0.5);
}

.result-box.aggressive li::before {
  color: #b388ff;
}

.content-box {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 15px;
  padding: 1.5rem;
  margin-top: 1.5rem;
  text-align: center;
}

/* 각 유형별 이미지 글로우 효과 */
.safe .character-icon img {
  filter: drop-shadow(0 0 10px rgba(41, 98, 255, 0.5));
}

.neutral .character-icon img {
  filter: drop-shadow(0 0 10px rgba(255, 196, 0, 0.5));
}

.aggressive .character-icon img {
  filter: drop-shadow(0 0 10px rgba(147, 51, 234, 0.5));
}

@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0px);
  }
}

.recommendation-section {
  margin-top: 3rem;
  text-align: center;
}

.recommendation-text {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  color: #fff;
}

.user-highlight {
  color: inherit; /* 각 투자 유형별 색상 상속 */
  font-weight: bold;
}

.safe .user-highlight {
  color: #4b83ff;
}

.neutral .user-highlight {
  color: #ffd700;
}

.aggressive .user-highlight {
  color: #b388ff;
}

.recommendation-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 1.8rem;
  border-radius: 50px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  width: fit-content;
}

.recommendation-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
}

.safe .recommendation-button {
  background: rgba(41, 98, 255, 0.2);
  border-color: rgba(41, 98, 255, 0.3);
}

.neutral .recommendation-button {
  background: rgba(255, 196, 0, 0.2);
  border-color: rgba(255, 196, 0, 0.3);
}

.aggressive .recommendation-button {
  background: rgba(147, 51, 234, 0.2);
  border-color: rgba(147, 51, 234, 0.3);
}

.recommendation-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
}

.safe .recommendation-button:hover {
  box-shadow: 0 0 20px rgba(41, 98, 255, 0.3);
}

.neutral .recommendation-button:hover {
  box-shadow: 0 0 20px rgba(255, 196, 0, 0.3);
}

.aggressive .recommendation-button:hover {
  box-shadow: 0 0 20px rgba(147, 51, 234, 0.3);
}

.fa-arrow-right {
  transition: transform 0.3s ease;
}

.recommendation-button:hover .fa-arrow-right {
  transform: translateX(5px);
}
</style>

<script>
export default {
  data() {
    return {
      userProfile: {
        nickname: "",
        user: {
          username: "",
        },
      },
      // ... 기존 data
    };
  },
  async created() {
    try {
      // 사용자 프로필 정보를 가져오는 API 호출
      const response = await this.axios.get("/api/user/profile/");
      this.userProfile = response.data;
    } catch (error) {
      console.error("프로필 정보를 불러오는데 실패했습니다:", error);
    }
  },
};
</script>
