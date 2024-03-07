import axios from "@/utils/http";

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
