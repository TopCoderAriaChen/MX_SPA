import type { PaginatedResponse } from "@/interfaces/api.interface";
import axios from "@/utils/http";
import { useAxios } from "@vueuse/integrations/useAxios";

export interface OrderStudent {
  id: string;
  username: string;
  display_name: string;
}

export interface OrderCourse {
  id: string;
  name: string;
}

export interface Order {
  id: string;
  student: OrderStudent;
  course: OrderCourse;
  created_time: Date;
  original_price: number;
  paid: boolean;
  paid_time: Date;
  paid_comment: string;
  paid_price: number;
}

export const createOrder = async (courseId: string, studentId: string) =>
  (
    await axios.post("/orders", {
      course: courseId,
      student: studentId,
    })
  ).data;

export const useOrderList = () =>
  useAxios<PaginatedResponse<Order>>(`/orders`, axios);

export const payOrder = async (
  orderId: string,
  comment: string,
  paid_price: number
) =>
  (
    await axios.put(`/orders/${orderId}/payment`, {
      paid: true,
      paid_comment: comment,
      paid_price: paid_price,
    })
  ).data;
