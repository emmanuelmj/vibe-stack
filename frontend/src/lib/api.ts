import axios from "axios";
import Cookies from "js-cookie";

const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1",
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true,
});

// Intercept requests to inject the token if it exists
api.interceptors.request.use(
    (config) => {
        // You can also use localStorage depending on your exact auth flow
        const token = Cookies.get("token") || (typeof window !== "undefined" ? localStorage.getItem("token") : null);

        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }

        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;
