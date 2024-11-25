<template>
  <div class="intro">
    <RouterLink to="/signup" class="nav-button">회원가입</RouterLink>
  <RouterLink to="/login" class="nav-button">로그인</RouterLink>
  <h2>서비스 소개</h2>
  <p>StockAdventure는 주식 정보를 제공하고, 투자 성향 테스트를 통해 개인의 투자 스타일을 이해할 수 있도록 돕습니다.</p>
  <p>회원 가입 후 다양한 주식 정보를 조회하고, 매매일지를 기록할 수 있습니다.</p>
  </div>
</template>
  
<style scoped>
.intro {
  padding: 20px;
  text-align: center;
}

.nav-button {
display: inline-block;
margin: 0 10px;
padding: 10px 20px;
text-decoration: none;
color: #333;
background-color: #f0f0f0;
border-radius: 5px;
transition: background-color 0.3s ease;
}

.nav-button:hover {
background-color: #ddd;
}

</style>