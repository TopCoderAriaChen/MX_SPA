import { useAuthStore } from '@/stores/auth';
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
          component: () => import("../views/HomeView.vue"),
          meta: {
            requiresAuth: true,
            title: "Home"
          }
        },
        {
          name: "courses",
          path: "/courses",
          component: () => import("../views/CoursesView.vue"),
          meta: {
            requiresAuth: true,
            title: "Course"
          }
        },
        {
          name: "course",
          path: "/courses/:id",
          component: () => import("../views/CourseView.vue"),
          meta: {
            requiresAuth: true,
            title: "Course Page"
          }
        }
      ]
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
      meta: {
        requiresAuth: false,
        title: "Login"
      }
    }
  ]
});

router.beforeEach((to) => {
  const AuthStore = useAuthStore();
  if (to.meta.requiresAuth && !AuthStore.isLoggedIn) {
    return {
      name: "login",  
      query: {redirect: to.fullPath},
    }
  }
});

router.afterEach((to) => {
  document.title = to.meta.title || to.name?.toString() || 
  "MoxueOnline";
});

export default router;
