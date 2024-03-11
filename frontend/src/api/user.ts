import type { PaginatedResponse } from "@/interfaces/api.interface";
import type { User } from "@/interfaces/user.interface";
import axios from "../utils/http";
import { useAxios } from "@vueuse/integrations/useAxios";

export interface CreateUserData {
  username: string;
  password: string;
  display_name: string;
  user_type: string;
  permissions?: Array<string>;
  telephone: string;
  campus: string;
  wx?: string;
  uni?: string;
  enrolled_courses?: Array<string>;
  abn?: string;
}

export enum USER_TYPE {
  ADMIN = "admin",
  STUDENT = "student",
  TEACHER = "teacher",
}

export const PERMISSIONS = {
  SYS_OWNER: "sys_owner",
  CAMPUS_ADMIN: "campus_admin",
  COURSE_ADMIN: "course_admin",
  USER_ADMIN: "user_admin",
  ORDER_ADMIN: "order_admin",
};

export const useUserList = () => useAxios<Array<User>>(`/users`, axios);

export const getCurrentUser = async () => {
  const response = await axios.get<User>("/auth");
  return response.data;
};

export const getAllTeachers = async () => {
  const { data } = await axios.get("/users");
  const teachers = data.filter((user: User) => user.user_type === "teacher");
  return teachers;
};

export const createUser = async (type: string, data: CreateUserData) => {
  let requestUrl = "";
  switch (type) {
    case USER_TYPE.ADMIN:
      requestUrl = "/admins";
      break;
    case USER_TYPE.TEACHER:
      requestUrl = "/teachers";
      break;
    case USER_TYPE.STUDENT:
      requestUrl = "/students";
      break;
    default:
    // throw exception message
  }

  const response = await axios.post(requestUrl, data);
  return response.data;
};

export const deleteUser = async ({ username }: { username: String }) => {
  const response = await axios.delete(`/users/${username}`);
  return response.data;
};

export const UpdateUser = async (username: string, data: CreateUserData) => {
  const response = await axios.post(`/users/${username}`, data);
  return response.data;
};

export const getUser = async (username: String) => {
  const response =await axios.get(`/users/${username}`);
  return response.data;
}
