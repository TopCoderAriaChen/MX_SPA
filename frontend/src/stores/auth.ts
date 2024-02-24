import { getCurrentUser } from "@/api/user";
import axios from "@/utils/http";
import { defineStore } from "pinia";

const PREFIX = import.meta.env.VITE_STORAGE_PREFIX;
const USER_INFO_PREFIX = PREFIX + "user_info";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    userInfo: JSON.parse(localStorage.getItem(USER_INFO_PREFIX) ?? 
    "null"),
  }),
  getters: {
    getUserInfo: (state) => state.userInfo,
    isLoggedIn: (state) => state.userInfo !== null
  },
  actions: {
    async login(username: string, password: string) {
      await axios.post("auth/login", {
        username,
        password
      });
      const user = await getCurrentUser();
      localStorage.setItem(USER_INFO_PREFIX, JSON.stringify(user));
    },
    async reload() {
        
    }
  }
});
