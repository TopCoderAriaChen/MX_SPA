import axios from "@/utils/http";
import { defineStore } from "pinia";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    userInfo: null,
  }),
  getters: {
    getUserInfo: (state) => state.userInfo,
    isLoggedIn: (state) => state.userInfo !== null,
  },
  actions: {
    async login(username: string, password: string) {
      const response = await axios.post("auth/login", {
        username,
        password,
      });
      console.log(response);
    },
  },
});
