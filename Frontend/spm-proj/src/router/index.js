import { createRouter, createWebHistory } from 'vue-router';
import HRHome from '../views/HRHome.vue';
import createJobListing from '../views/createJobListing.vue';
import landingPage from '../views/LandingPage.vue';
import StaffPage from '../views/StaffPage.vue';
import createSuccess from '../views/createSuccess.vue';
import updateRoleListing from '../views/updateRoleListing.vue';

const routes = [
    // route: landing page
    {
        path: '/',
        name: 'landingPage',
        component: () => import('../views/LandingPage.vue')
    },

    {
    path: '/create-job-listing',
    name: 'createJobListing',
    component: createJobListing,
    },

    {
      path: '/create-job-listing/createSuccess',
      name: 'createSuccess',
      component: createSuccess,
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

    {
      path: '/updateRoleListing',
      name: 'updateRoleListing',
      component: updateRoleListing,
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
