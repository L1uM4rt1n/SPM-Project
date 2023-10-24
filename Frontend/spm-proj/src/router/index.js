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

    // route: create role listing page
    {
        path: '/createJobListing',
        name: 'CreateJobListing',
        component: () => import('../views/HR/createJobListing.vue'),

    },

    //route: profile page
    {
        path: '/profile',
        name: 'profile-page',
        component: ()=> import('../views/profile.vue'),

    }

];

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes,
    }
)

export default router
