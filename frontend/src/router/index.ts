import { createRouter, createWebHistory } from "vue-router";
import Layout from "../layout/index.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "layout",
      redirect: "/home",
      component: Layout,
      children: [
        {
          name: "home",
          path: "/home",
          component: () => import("../views/HomeView.vue")
        },
        {
          name: "courses",
          path: "/courses",
          component: () => import("../views/CoursesView.vue")
        },
        {
          name: "course",
          path: "/courses/:id",
          component: () => import("../views/CourseView.vue")
        }
      ]
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue")
    }
  ]
});

export default router;
