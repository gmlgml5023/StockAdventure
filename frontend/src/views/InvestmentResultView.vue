<template>
    <div class="result-container">
      <h1>투자성향 분석 결과</h1>
      <div class="result-card">
        <h2>{{ getStyleName }}</h2>
        <p>{{ getStyleDescription }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
//   import { computed } from 'vue'
//   import { useRoute } from 'vue-router'
  
//   const route = useRoute()
  
//   const getStyleName = computed(() => {
//     const type = Number(route.params.type)
//     switch(type) {
//       case 1: return '안정형 투자자'
//       case 2: return '위험중립형 투자자'
//       case 3: return '공격투자형 투자자'
//       default: return '분석 결과 없음'
//     }
//   })
  
//   const getStyleDescription = computed(() => {
//     const type = Number(route.params.type)
//     switch(type) {
//       case 1: return '안정적인 수익을 추구하며 원금 보존을 중시하는 투자자입니다.'
//       case 2: return '적절한 위험을 감수하며 균형 잡힌 수익을 추구하는 투자자입니다.'
//       case 3: return '높은 수익을 위해 적극적인 투자를 선호하는 투자자입니다.'
//       default: return ''
//     }
//   })
  </script>
  
  <style scoped>
  .result-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .result-card {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  </style>