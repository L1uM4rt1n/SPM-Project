import { createRouter, createWebHistory } from 'vue-router';
import HRHome from '../views/HRHome.vue';
import createJobListing from '../views/createJobListing.vue';
import Login from '../views/Login.vue';
const routes = [
  // Other routes
    {
    path: '/create-job-listing',
    name: 'createJobListing',
    component: createJobListing,
    },

    {
    path: '/',
    name: 'HRHome',
    component: HRHome,
    },

    {
      path: '/login',
      name: 'Login',
      component: Login,
      },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
