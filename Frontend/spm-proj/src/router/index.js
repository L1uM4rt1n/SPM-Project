import { createRouter, createWebHistory } from 'vue-router';
import HRHome from '../views/HRHome.vue';
import createJobListing from '../views/createJobListing.vue';

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
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
