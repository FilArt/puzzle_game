// Composables
import { useAppStore } from "@/store/app";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/HomeScreen.vue"),
      },
      {
        path: "game",
        name: "Game",
        component: () =>
          import(/* webpackChunkName: "game" */ "@/views/GameScreen.vue"),
        beforeEnter: (to, from, next) => {
          const appStore = useAppStore();
          if (!appStore.username || !appStore.username.length) next("/login");
          else next();
        },
      },
      {
        path: "login",
        name: "Login",
        component: () =>
          import(/* webpackChunkName: "login" */ "@/views/Login.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
