import { useAxios } from "@vueuse/integrations/useAxios";
import axios from "../utils/http";

export interface Course {
    id: string;
    name: string;
    uni_course_code: string;
    description: string;
    teacher: Teacher;
    campus: Campus;
    created_time: string;
    publish_time: string;
    original_price: number;
    cover_image: string;
    lectures: Lecture[];
    enrolled_students: EnrolledStudent[];
}

export interface Teacher {
    id: string;
    display_name: string;
}

export interface Campus {
    id: string;
    name: string;
}

export interface Lecture {
  id: string;
  title: string;
  streaming_url: string;
  recording_url: string;
  scheduled_at: string;
}

export interface EnrolledStudent {
  id: string;
  username: string;
  display_name: string;
}

export interface CreateLectureData {
  title: string;
  streaming_url: string;
  recording_url: string;
  scheduled_at: string;
}

export const useCourse = (course_id: string) =>
    useAxios<Course>(`/courses/${course_id}`, axios);


export const deleteLecture = async (course_id: string, lecture_id: string) => {
  await axios.delete(`/courses/${course_id}/lectures/${lecture_id}`);
};

export const createLecture = async (
  course_id: string,
  data: CreateLectureData
) => 
  await (
    await axios.post<String>(`/courses/${course_id}/lectures`, data)
  ).data;