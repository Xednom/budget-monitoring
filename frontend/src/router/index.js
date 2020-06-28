import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../app/Home.vue";

Vue.use(VueRouter);

const requireAppRoutes = require.context(
  '.',
  true,
  /routes.js$/
);

function mergeAppRoutes () {
  //Merges all routes.js files in the project!
  let routes = [];
  requireAppRoutes.keys().forEach((fileName) => {
    const foundRoutes = requireAppRoutes(fileName);
    routes = routes.concat(foundRoutes.default)
  });
  return routes;
}

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../app/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
