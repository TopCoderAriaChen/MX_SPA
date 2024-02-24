import type { User } from "@/interfaces/user.interface";
import axios from "../utils/http";

export const getCurrentUser = async () => {
  const response = await axios.get<User>("/auth");
  return response.data;
};
