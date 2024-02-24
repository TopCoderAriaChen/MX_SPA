import axios from "axios";

const axiosInstance = axios.create({
  timeout: 5000,
  baseURL: import.meta.env.VITE_API_BASE,
});

axiosInstance.interceptors.request.use((config) => {
  console.withCredentials = true;
  return config
});
export default axiosInstance;
