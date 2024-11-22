<template>
    <div class="investment-test">
      <h1>주식 투자성향 테스트</h1>
      <form @submit.prevent="submitTest">
        <div v-for="(question, index) in questions" :key="index" class="question-block">
          <h3>{{ question.title }}</h3>
          <p>{{ question.description }}</p>
          <div v-for="(option, optionIndex) in question.options" :key="optionIndex" class="option">
            <input 
              type="radio" 
              :id="`q${index}_${optionIndex}`"
              :name="`question${index}`"
              :value="optionIndex + 1"
              v-model="answers[index]"
              required
            >
            <label :for="`q${index}_${optionIndex}`">{{ option }}</label>
          </div>
        </div>
        <button type="submit" class="submit-btn">제출하기</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from '@/plugins/axios'
  import { useAuthStore } from '@/stores/auth'
  
  const router = useRouter()
  const authStore = useAuthStore()
  const answers = ref(Array(7).fill(null))
  
  const questions = [
    {
      title: '1. 투자 기간',
      description: '투자 기간은 어느 정도로 생각하고 계십니까?',
      options: [
        '3년 이상',
        '2-3년',
        '1-2년',
        '1년 미만'
      ]
    },
    {
      title: '2. 투자 목표',
      description: '투자의 주된 목표는 무엇입니까?',
      options: [
        '원금 보존과 안정적인 수익',
        '적절한 수익과 위험의 균형',
        '높은 수익 추구',
        '매우 공격적인 자산 증식'
      ]
    },
    {
      title: '3. 수입원',
      description: '다음 중 당신의 수입원을 가장 잘 나타내고 있는 것은 어느 것입니까?',
      options: [
        '현재 안정적인 수입이 있으며, 향후 크게 증가할 것으로 예상',
        '현재 일정한 수입이 발생하고 있으며, 향후 현재 수준을 유지하거나 약간 증가할 것으로 예상',
        '현재 일정한 수입이 발생하고 있으나, 향후 감소하거나 불안정할 것으로 예상',
        '현재 일정한 수입원이 없으며, 연금이나 저축이 주 수입원임'
      ]
    },
    {
      title: '4. 자산 비중',
      description: '주식 투자에 할애할 수 있는 자산 비중',
      options: [
        '10% 미만',
        '10-30%',
        '30-50%',
        '50% 이상'
      ]
    },
    {
      title: '5. 주가 하락 시 반응',
      description: '주식 가치가 30% 하락했을 때의 반응',
      options: [
        '즉시 모든 주식을 매도한다',
        '일부를 매도하고 나머지는 보유한다',
        '그대로 보유한다',
        '추가 매수를 고려한다'
      ]
    },
    {
      title: '6. 선호하는 투자 전략',
      description: '선호하는 투자 전략',
      options: [
        '안정적인 대형 우량주 위주',
        '배당주 중심의 투자',
        '성장 가능성이 있는 중소형주',
        '신기술/신산업 관련 주식'
      ]
    },
    {
      title: '7. 원금손실에 대한 태도',
      description: '원금 손실에 대해 어떻게 생각하십니까?',
      options: [
        '어떤 경우에도 원금 손실은 받아들일 수 없다',
        '5% 미만의 아주 작은 원금 손실은 감수할 수 있다',
        '10-20% 정도의 원금 손실은 감수할 수 있다',
        '높은 수익을 위해 30% 이상의 상당한 원금 손실도 감수할 수 있다'
      ]
    }
  ]
  
  const calculateInvestmentStyle = (score) => {
    if (score <= 23) return 1 // 안정형 투자자
    if (score <= 37) return 2 // 위험중립형 투자자
    return 3 // 공격투자형 투자자
  }
  
  const submitTest = async () => {
    const totalScore = answers.value.reduce((sum, current) => sum + current, 0)
    const investmentStyle = calculateInvestmentStyle(totalScore)

    try {
    // 현재 사용자의 투자성향 정보 조회
    const userResponse = await axios.get('http://127.0.0.1:8000/investment_style/result/', {
        headers: {
            'Authorization': `Token ${authStore.token}`
        },
        withCredentials: true
    })

    // 투자성향이 없는 경우도 정상 응답으로 처리
    const method = userResponse.data.style_id ? 'put' : 'post'
        
        const response = await axios({
            method: method,
            url: 'http://127.0.0.1:8000/investment_style/test/',
            data: {
                style_id: investmentStyle
            },
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authStore.token}`
            },
            withCredentials: true
        })

        router.push({ 
            name: 'investment-result', 
            params: { 
                type: investmentStyle 
            }
        })
    } catch (error) {
    console.error('투자성향 저장 실패:', error)
    if (error.response?.status === 401) {
        router.push('/login')
    }
}}
</script>
  
  <style scoped>
  .investment-test {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .question-block {
    margin-bottom: 30px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  
  .option {
    margin: 15px 0;
    display: flex;
    align-items: flex-start;
  }
  
  .option input[type="radio"] {
    margin-right: 10px;
    margin-top: 5px;
  }
  
  .option label {
    line-height: 1.4;
  }
  
  .submit-btn {
    width: 100%;
    padding: 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 20px;
  }
  
  .submit-btn:hover {
    background-color: #45a049;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 30px;
  }
  
  h3 {
    color: #2c3e50;
    margin-bottom: 10px;
  }
  </style>