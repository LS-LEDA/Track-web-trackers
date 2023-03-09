import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ResultView from "../views/ResultView.vue";
import AboutView from "../views/AboutView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/results/:url",
      name: "results",
      component: ResultView,
    },
    {
      path: "/about",
      name: "about",
      component: AboutView
    }
  ],
});

export default router;
