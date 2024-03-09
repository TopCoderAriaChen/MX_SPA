import axios, { AxiosError, type AxiosRequestHeaders } from "axios";
import { useCookies } from "@vueuse/integrations/useCookies";
import type { MessageApiInjection } from "naive-ui/es/message/src/MessageProvider";
import router from "@/router";
import { useAuthStore } from "@/stores/auth";

interface Headers extends AxiosRequestHeaders {
  "X-CSRF-TOKEN": string;
}
const CSRF_ACCESS_TOKEN = "csrf_access_token";
const cookies = useCookies([CSRF_ACCESS_TOKEN]);

const axiosInstance = axios.create({
  timeout: 5000,
  baseURL: import.meta.env.VITE_API_BASE,
});

axiosInstance.interceptors.request.use((config) => {
  config.withCredentials = true;
  const token = cookies.get<String>(CSRF_ACCESS_TOKEN);
  config.headers = {
    ...config.headers,
    "X-CSRF-TOKEN": token,
  } as Headers;
  return config;
});

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    const message = (window as any).$message as MessageApiInjection;
    if (error instanceof AxiosError && error.response) {
      switch (error.response.status) {
        case 401:
          if (router.currentRoute.value.name !== "login") {
            const authStore = useAuthStore();
            authStore.logout();
            router.replace({
              path: "/login",
              query: {
                redirect: router.currentRoute.value.fullPath,
              },
            });
          } else {
            message.error(error.response.data["message"] || "Unauthorized");
          }
          break;
        default:
          message.error(error.response.data.message || "Unkown Error");
      }
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
