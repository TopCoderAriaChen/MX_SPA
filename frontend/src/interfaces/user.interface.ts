import type { CourseBasicInfo } from "@/api/course";

export interface User {
  id: string;
  username: string;
  password: string | null;
  display_name: string;
  telephone: string;
  campus: {
    id: string;
    name: string;
  };
  created_at: string;
  wx?: string;
  uni?: string;
  permissions?: [string];
  user_type: string;
  abn?: string;
  enrolled_courses?: CourseBasicInfo[];
}
