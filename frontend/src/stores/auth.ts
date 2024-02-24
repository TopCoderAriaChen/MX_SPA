import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    userInfo: null,
  }),
  getters: {
    getUserInfo: (state) => state.userInfo,
    isLoggedIn: (state) => state.userInfo !== null,
  },
  actions: {
    login(username: string, password: string) {
      console.log(username);
      console.log(password);
    },
  },
});
