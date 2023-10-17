import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  // Other routes
    {
    path: '/',
    name: 'landingPage',
    component: () => import('../views/LandingPage.vue'),
    },


    // {
    // path: '/create-job-listing',
    // name: 'createJobListing',
    // component: createJobListing,
    // },

    {
    path: '/hr-home',
    name: 'HRHome',
    component: () => import('../views/HR/HRHome.vue'),
    },

    {
    path: '/staff-home',
    name: 'StaffHome',
    component: () => import('../views/Staff/StaffHome.vue'),
    },

    {
      path: '/login-page',
      name: 'LoginPage',
      component: () => import('../views/LoginPage.vue'),
    },

    // {
    // path: '/role/:slug',
    // component: RoleDetails
    // }
    


    
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;