<template>
  <div class="container">
    <div class="nav-container">
      <h1 class="logo">StockVenture</h1>
      <nav class="nav-menu">
        <RouterLink to="/signup" class="nav-button">회원가입</RouterLink>
        <RouterLink to="/login" class="nav-button">로그인</RouterLink>
      </nav>
    </div>

    <section class="scroll-section" id="main">
      <div class="content fade-in">
        <h1>Stock Venture</h1>
        <h2>우주로 떠나는 주식 투자 여행</h2>
        <br />
        <p>
          안녕하세요, 투자자 여러분!<br />
          StockVenture에 오신 것을 환영합니다.<br /><br />
          우리는 여러분의 투자 여정을<br />
          로켓을 타고 우주 여행을 떠나는 것처럼,
          <br />
          더 높은 수익률을 향해 함께 날아오르는 경험으로 만들어드립니다.<br /><br />
        </p>
        <div class="rocket-icon">🚀</div>
      </div>
    </section>

    <!-- 투자 성향 섹션 -->
    <section class="scroll-section" id="investment-style">
      <div class="content fade-in">
        <h2>🚀 투자 성향에 맞춘 맞춤형 종목 추천</h2>
        <div class="section-content">
          <p>
            투자 성향을 탐색하는 첫 번째 단계!<br /><br />
            안정형, 위험중립형, 공격투자형으로 나누어진 맞춤형 테스트로,<br />
            당신에게 가장 적합한 투자 종목을 추천해드립니다.<br /><br />
            안정적인 배당주부터 고수익을 노리는 성장주까지,<br />
            여러분의 투자 로켓을 우주로 쏘아올릴 준비가 되어 있습니다!<br /><br />
            지금 바로 테스트를 시작하고,<br />
            나만의 투자 여정을 시작해보세요!
          </p>
        </div>
      </div>
    </section>

    <!-- 매매일지 섹션 -->
    <section class="scroll-section" id="trading-journal">
      <div class="content fade-in">
        <h2>📖 매매일지: 여러분의 투자 여정을 기록하라</h2>
        <!-- 섹션 내용 -->
        <p>
          매매일지 기능을 통해 여러분의 투자 여정을 기록하세요.<br /><br />
          날짜, 종목명, 매매 이유와 결과를 정리함으로써<br />
          과거의 경험에서 배우고,<br />
          향후 투자 전략을 더욱 견고히 할 수 있습니다.<br /><br />
          반복되는 실수를 줄이고, 자신만의 투자 원칙을 세워보세요!<br />
        </p>
      </div>
    </section>

    <!-- 커뮤니티 섹션 -->
    <section class="scroll-section" id="community">
      <div class="content fade-in">
        <h2>💬 커뮤니티와 함께하는 종목 토론</h2>
        <!-- 섹션 내용 -->
        <p>
          커뮤니티는 여러분이 다른 투자자들과 소통하고,<br />
          전략을 공유할 수 있는 공간입니다.<br /><br />
          함께 투자 아이디어를 나누고,<br />
          시장 전망을 이야기하며,<br />
          함께 더 높은 목표를 향해 나아가세요!
        </p>
      </div>
    </section>

    <!-- 마지막 섹션 -->
    <section class="scroll-section" id="final">
      <div class="content fade-in">
        <h2>
          StockVenture와 함께,<br />
          여러분의 수익률을 우주로 쏘아올려 보세요!<br /><br />
          이제는 주식 탐사 여행을 떠날 시간입니다.<br />
          새로운 투자 세계로의 모험을 시작하세요!
        </h2>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  mounted() {
    // Intersection Observer를 사용한 스크롤 애니메이션
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
          }
        });
      },
      { threshold: 0.1 }
    );

    document.querySelectorAll(".fade-in").forEach((el) => observer.observe(el));

    // 스무스 스크롤 기능 추가
    function smoothScroll(target, duration = 2000) {
      const targetPosition = target.getBoundingClientRect().top;
      const startPosition = window.pageYOffset;
      const distance = targetPosition - startPosition;
      let startTime = null;

      function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
      }

      function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t + b;
        t--;
        return (-c / 2) * (t * (t - 2) - 1) + b;
      }

      requestAnimationFrame(animation);
    }

    // 스크롤이 필요한 요소에 이벤트 리스너 추가
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
          smoothScroll(target);
        }
      });
    });
  },
};
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.container {
  text-align: center;
  max-width: 100%;
  margin: 0;
  padding: 0;
  scroll-snap-type: y mandatory;
  height: 100vh;
  overflow-y: scroll;
  overflow-x: hidden;
}

.scroll-section {
  height: 100vh;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  width: 100%;
}

.content {
  margin: 0 auto;
  max-width: 1200px;
  padding: 0 20px;
  width: 100%;
  box-sizing: border-box;
}

.intro {
  padding: 20px;
  text-align: center;
}

.nav-button {
  display: inline-block;
  margin: 0 10px;
  padding: 10px 20px;
  font-size: 20px;
  text-decoration: none;
  color: #333;
  background-color: #f0f0f0;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-button:hover {
  background-color: #ddd;
}

.section-content {
  text-align: center;
  font-size: 1.2rem;
  line-height: 1.8;
  margin: 2rem auto;
  max-width: 800px;
}

.section-content p {
  margin: 0 auto;
}

h1 {
  font-size: 3.3rem;
}

h2 {
  font-size: 2.2rem;
  margin-bottom: 1.5rem;
}

p {
  font-size: 1.5rem;
  line-height: 1.8;
  margin: 1rem 0;
}

h3 {
  font-size: 1.65rem;
  line-height: 1.6;
  margin: 2rem 0;
}

.fixed-auth-buttons {
  position: fixed;
  top: 150px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  display: flex;
  gap: 20px;
}

.button {
  text-decoration: none;
  padding: 10px 20px;
  border: 2px solid #fff;
  border-radius: 5px;
  color: #fff;
  transition: all 0.3s ease;
}

.button:hover {
  background-color: #fff;
  color: #000;
}

.nav-container {
  margin: 0 auto;
  padding: 20px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(240, 219, 55, 0.2);
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
}

.logo {
  color: #f0db37;
  font-size: 32px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.nav-menu {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 15px;
  padding: 10px 0;
}

.nav-button {
  padding: 10px 20px;
  text-decoration: none;
  color: #f0db37;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(240, 219, 55, 0.4);
  border-radius: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
  backdrop-filter: blur(5px);
}

.nav-button:hover {
  transform: translateY(-2px);
  background: rgba(240, 219, 55, 0.2);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.2);
}

.scroll-section:first-child {
  padding-top: 180px;
}

@media (max-width: 768px) {
  .nav-menu {
    flex-direction: column;
    align-items: center;
  }

  .nav-button {
    width: 100%;
    text-align: center;
  }
}

/* 스크롤바 전체 스타일링 */
.container::-webkit-scrollbar {
  width: 10px;
}

/* 스크롤바 트랙 (배경) */
.container::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}

/* 스크롤바 핸들 (이동하는 부분) */
.container::-webkit-scrollbar-thumb {
  background: rgba(240, 219, 55, 0.6);
  border-radius: 5px;
}

/* 스크롤바 핸들 호버 효과 */
.container::-webkit-scrollbar-thumb:hover {
  background: rgba(240, 219, 55, 0.8);
}

/* Firefox를 위한 스크롤바 스타일링 */
.container {
  scrollbar-width: thin;
  scrollbar-color: rgba(240, 219, 55, 0.6) rgba(255, 255, 255, 0.1);
}
</style>
