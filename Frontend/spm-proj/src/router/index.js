import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    // route: landing page
    {
        path: '/',
        name: 'landingPage',
        component: () => import('../views/LandingPage.vue')
    },

    // route: individual role listing
    {
        path: '/staff-home/role-listings',
        name: 'roleListings',
        component: () => import('../views/Staff/RoleListing.vue')
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
];

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes,
    }
)

export default router
