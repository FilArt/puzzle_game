import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8000",
});

const axiosPlugin = {
  install(app) {
    app.config.globalProperties.$api = api;
  },
};

export default axiosPlugin;
