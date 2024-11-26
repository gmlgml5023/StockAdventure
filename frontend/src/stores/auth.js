import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAuthStore = defineStore('auth', () => {
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);
    const username = ref(null); // 사용자 이름 상태 추가
    const isLogin = computed(() => !!token.value);
    const router = useRouter();
    const investment_style = ref(null);

    // isAuthor 함수 정의 추가
    const isAuthor = (articleUsername) => {
      return username.value === articleUsername;
    };


    // 회원가입 요청 액션
    const signUp = function (payload) {
      const { username, password1, password2 } = payload;
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: { username, password1, password2 }
      })
      .then(() => {
        // 회원가입 성공 시 로그인
        logIn({ username, password: password1 });
      })
      .catch((err) => {
        console.error('회원가입 실패:', err);
      });
    };

    // 로그인 요청 액션
    const logIn = function (payload) {
      const { username: loginUsername, password } = payload;

      // 로그인 요청
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: { username: loginUsername, password }
      })
      .then((res) => {
        token.value = res.data.key; // 로그인 성공 시 토큰 저장

        // 사용자 기본 정보 요청
        return axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`, // 사용자 기본 정보 요청
          headers: { Authorization: `Token ${token.value}` }
        });
      })
      .then((userRes) => {
        username.value = userRes.data.username; // 서버로부터 받은 사용자 이름 저장

        // 추가 사용자 정보 요청
        return axios({
          method: 'get',
          url: `${API_URL}/accounts/${username.value}/`, // 추가 사용자 정보 요청
          headers: { Authorization: `Token ${token.value}` }
        });
      })
      .then((additionalUserRes) => {
        investment_style.value = additionalUserRes.data.investment_style; // 투자 스타일 저장

        console.log("추가 사용자 정보:", additionalUserRes.data); // 디버깅용 출력
        console.log("투자 스타일:", investment_style.value); // 디버깅용 출력

        // 사용자 정보에서 투자 스타일 확인
        if (!investment_style.value) {
          // 투자 스타일이 비어있으면 검사 페이지로 리다이렉트
          router.push({ path: "/investment_style/test" });
        } else {
          // 투자 스타일이 존재하면 홈 페이지로 이동
          router.push({ name: "home" });
        }
      })
      .catch((err) => {
        console.error('로그인 실패:', err);
      });
    };

    // 로그아웃
    const logOut = function () {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: { Authorization: `Token ${token.value}` }
      })
      .then(() => {
        token.value = null;
        username.value = null;
        router.push({ name: "intro" }); // 로그아웃 후 intro 페이지로 리다이렉트
      })
      .catch((err) => {
        console.error('로그아웃 실패:', err);
      });
    };

    return { 
        API_URL, 
        signUp, 
        logIn, 
        token, 
        isLogin, 
        logOut, 
        username,
        isAuthor  // isAuthor 함수 추가
    };
}, {
    persist: {
        storage: sessionStorage
    }
});