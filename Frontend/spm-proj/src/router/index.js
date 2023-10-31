import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    // route: landing page
    {
        path: '/',
        name: 'landingPage',
        component: () => import('../views/LandingPage.vue'),
    },

    // route: login page
    {
        path: '/login-page',
        name: 'LoginPage',
        component: () => import('../views/LoginPage.vue'),
    },

    // route: HR home page
    {
        path: '/hr-home',
        name: 'HRHome',
        component: () => import('../views/HR/HRHome.vue'),
    },

    // route: staff home page
    {
        path: '/staff-home',
        name: 'StaffHome',
        component: () => import('../views/Staff/StaffHome.vue'),
    },

    //route: update role listing
    {
      path: '/hr-home/update-role-listing/:roleId',
      name: 'updateRoleListing',
      component: () => import('../views/updateRoleListing.vue')
  },

    // route: create job listing page
    {
        path: '/hr-home/create-job-listing',
        name: 'createJobListing',
        component: () => import('../views/createJobListing.vue')
    },

    // route: manage listings page
    {
        path: '/hr-home/manage-listings/:roleId',
        name: 'manageListings',
        component: () => import('../views/manageListings.vue')
    },

];

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes,
    }
)

export default router
