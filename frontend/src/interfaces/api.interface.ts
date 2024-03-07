export interface PaginatedResponse<T> {
  total: number;
  page: number;
  pages: number;
  limit: number;
  items: T[];
}
