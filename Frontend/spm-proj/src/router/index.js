import { createRouter, createWebHistory } from 'vue-router'
import landingPage from '../views/LandingPage.vue'
import roleListings from '../views/RoleListing.vue'
import HRHome from '../views/HRHome.vue'

const routes = [
    // route: landing page
    {
        path: '/',
        name: 'landingPage',
        component: landingPage
    },

    // route: individual role listing
    {
        path: '/role-listings',
        name: 'roleListings',
        component: roleListings
    },
    // route: HR home page
    {
        path: '/hr-home',
        name: 'HRHome',
        component: HRHome
    }
];

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes,
    }
)

export default router
