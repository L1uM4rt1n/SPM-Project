import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    // route: landing page
    {
    path: '/',
    name: 'landingPage',
    component: () => import('../views/LandingPage.vue'),
    },

    // route: HR home page
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

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes,
    }
)

export default router
