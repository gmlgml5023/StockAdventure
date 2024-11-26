<template>
  <div class="investment-result">
    <h1>투자 성향 검사 결과</h1>
    <div v-if="investmentStyle === 1">
      <h2>안정형 투자자</h2>
      <p>당신은 안정적인 투자를 선호하는 투자자입니다.</p>
    </div>
    <div v-else-if="investmentStyle === 2">
      <h2>위험중립형 투자자</h2>
      <p>당신은 적절한 위험을 감수하면서 수익을 추구하는 투자자입니다.</p>
    </div>
    <div v-else-if="investmentStyle === 3">
      <h2>공격투자형 투자자</h2>
      <p>당신은 높은 수익을 위해 위험을 감수하는 투자자입니다.</p>
    </div>
    <div v-else>
      <p>투자 성향을 확인할 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const investmentStyle = ref(null);

onMounted(() => {
  // URL 쿼리 파라미터에서 investment_style_id를 가져옵니다
  investmentStyle.value = parseInt(route.query.investment_style_id);
});
</script>

<style scoped>
.investment-result {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #f6f2f2;
  margin-bottom: 20px;
}

h2 {
  color: #e6e6e6;
  margin-bottom: 10px;
}

p {
  color: #e2e2e2;
  line-height: 1.6;
}
</style>
