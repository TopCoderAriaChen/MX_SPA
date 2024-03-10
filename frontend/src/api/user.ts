
import type { User } from "@/interfaces/user.interface";
import axios from "../utils/http";

export const getCurrentUser = async () => {
  const response = await axios.get<User>("/auth");
  return response.data;
};

export const getAllTeachers =async () => {
  const {data} = await axios.get("/users")
  const teachers = data.filter((user:User
    )=>user.user_type==="teacher")
  return teachers
}
