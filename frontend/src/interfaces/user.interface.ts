
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
  user_type: String;
  abn?: String;
}
