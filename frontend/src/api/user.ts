import axios from "../utils/http";

export const getCurrentUser = async () => {
  const response = await axios.get("/auth");
  return response.data;
};
