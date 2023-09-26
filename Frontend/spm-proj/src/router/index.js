import { createRouter, createWebHistory } from 'vue-router';
import HRHome from '../views/HRHome.vue';
import createJobListing from '../views/createJobListing.vue';
import landingPage from '../views/LandingPage.vue';
import StaffHome from '../views/StaffHome.vue';

const routes = [
  // Other routes
    {
    path: '/',
    name: 'landingPage',
    component: landingPage,
    },

    {
    path: '/create-job-listing',
    name: 'createJobListing',
    component: createJobListing,
    },

    {
    path: '/HRHome',
    name: 'HRHome',
    component: HRHome,
    },

    {
      path: '/StaffHome',
      name: 'StaffHome',
      component: StaffHome,
      },

    
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
