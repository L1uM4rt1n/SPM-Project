import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    // route: landing page
    {
        path: '/',
        name: 'landingPage',
        component: () => import('../views/LandingPage.vue')
    },

    // route: HR home page
    {
        path: '/hr-home',
        name: 'HRHome',
        component: () => import('../views/HR/HRHome.vue')
    },

    // route: Staff home page
    {
        path: '/staff-home',
        name: 'StaffHome',
        component: () => import('../views/Staff/StaffHome.vue')
    },

    // route: individual role listing
    {
        path: '/staff-home/role/:id',
        name: 'roleListing',
        component: () => import('../views/Staff/RoleListing.vue'),
        props: (route) => ({ roleId: route.params.id })
    },
];

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes,
    }
)

export default router
