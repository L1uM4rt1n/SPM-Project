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

    // route: individual role listing
    {
        path: '/staff-home/role/:id',
        name: 'roleListing',
        component: () => import('../views/Staff/RoleListing.vue'),
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
        

    },
    {
        path: '/hr-home/update-role-listing/:roleId',
        name: 'updateRoleListing',
        component: () => import('../views/HR/updateRoleListing.vue')
    },

  
      // route: manage listings page
      {
          path: '/hr-home/manage-listings/:roleId',
          name: 'manageListings',
          component: () => import('../views/manageListings.vue')
      },


];
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
  // Global navigation guards
  router.beforeEach((to, from, next) => {
    // Logic for beforeEach guard
    next();
  });
  
  router.beforeResolve((to, from, next) => {
    // Logic for beforeResolve guard
    next();
  });
  
  export default router;

