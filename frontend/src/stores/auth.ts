import { getCurrentUser } from "@/api/user";
import axios from "@/utils/http";
import { defineStore } from "pinia";
import { useLocalStorage, StorageSerializers } from "@vueuse/core";
import type { User } from "@/interfaces/user.interface";

const PREFIX = import.meta.env.VITE_STORAGE_PREFIX;
const USER_INFO_PREFIX = PREFIX + "user_info";

export const useAuthStore: any = defineStore({ 
  id: "auth",
  state: () => ({
    userInfo: useLocalStorage<User | null>(USER_INFO_PREFIX, null, {
      serializer: StorageSerializers.object,
    }),
  }),
  getters: {
    getUserInfo: (state) => state.userInfo,
    isAdmin: (state) => state.userInfo?.user_type === "admin",
    isLoggedIn: (state) => state.userInfo !== null,
  },
  actions: {
    async login(username: string, password: string) {
      await axios.post("auth/login", {
        username,
        password,
      });
      const user = await getCurrentUser();
      this.userInfo = user;
    },
    async reload() {
      const user = await getCurrentUser();
      this.userInfo = user;
    },
    async logout() {
      this.userInfo = null;
    },
  },
});
