import { createRouter, createWebHistory } from 'vue-router';
import HRHome from '../views/HRHome.vue';
import landingPage from '../views/LandingPage.vue';
import StaffPage from '../views/StaffPage.vue';

const routes = [
  // Other routes
    {
    path: '/',
    name: 'landingPage',
    component: landingPage,
    },

    {
    path: '/HRHome',
    name: 'HRHome',
    component: HRHome,
    },

    {
    path: '/StaffPage',
    name: 'StaffPage',
    component: StaffPage,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;