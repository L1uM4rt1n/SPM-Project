<template>

  <div id="app">
    <!-- Header content -->
    <header>

    </header>

    <!-- Navigation Bar content-->
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img src="./img/ondeh.jpeg" width="50" height="50" alt="">  <i>Ondeh Ondeh</i>
          </a>
          <a class="navbar-brand" href="#">
          <img src="./img/user.png"  class="rounded-circle" width="50" height="50" alt="">
        </a>
      </div>
    </nav>

    <main>
        <!-- Contains the main content of the webpage-->
      <div>
      <router-view></router-view>
      </div>

    </main>

    <footer>
      <!-- Footer content -->
    </footer>

  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS
// import router from "./router";
import { createRouter, createWebHistory } from 'vue-router';


export default {
  name: 'App',

  methods: {

  },

// Configure the Vue Router instance
router: createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
      // Define your routes here
      {
        path: '/hr-home',
        name: 'HRHome',
        component: () => import('./views/HRHome.vue'), // Example: Import your Home component
      },
    ],
  }),
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
