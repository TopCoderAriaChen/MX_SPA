import { User } from "./user.interface";
export interface User {
  username: String;
  password: String | null;
  display_name: String;
  telephone: String;
  campus: String;
  created_at: String;
  wx?: String;
  uni?: String;
  permissions?: [String];
  User_type: String;
  abn?: String;
}
