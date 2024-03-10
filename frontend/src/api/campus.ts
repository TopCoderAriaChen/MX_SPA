import axios from "../utils/http";

export const getAllCampus = async () => {
  const { data } = await axios.get("/campus");
  return data;
};
