import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);
    const username = ref(null); // 사용자 이름 상태 추가
    const isLogin = computed(() => !!token.value);
    const router = useRouter();

    // 회원가입 요청 액션
    const signUp = function (payload) {
      const { username, password1, password2 } = payload;
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: { username, password1, password2 }
      })
      .then(() => {
        logIn({ username, password: password1 });
      })
      .catch((err) => {
        console.error('회원가입 실패:', err);
      });
    };

    // 로그인 요청 액션
    const logIn = function (payload) {
      const { username: loginUsername, password } = payload;
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: { username: loginUsername, password }
      })
      .then((res) => {
        token.value = res.data.key;

        return axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: { Authorization: `Token ${token.value}` }
        });
      })
      .then((userRes) => {
        username.value = userRes.data.username; // 서버로부터 받은 사용자 이름 저장
        router.push({ name: "home" });
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
        username.value = null; // 로그아웃 시 사용자 이름 초기화
        router.push({ name: "home" });
      })
      .catch((err) => {
        console.error('로그아웃 실패:', err);
      });
    };

    return { API_URL, signUp, logIn, token, isLogin, logOut, username };
  },
  { persist: true }
);