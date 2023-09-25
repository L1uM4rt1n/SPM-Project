<template>

  <div id="app">
    <!-- Header content -->
    <header>

    </header>


    <!-- Navigation Bar content-->
    <nav class="navbar navbar-light border-bottom border-dark">
      <div class="container-fluid">
        <router-link :to="{ name: 'landingPage' }">
        <a class="navbar-brand btn" href="#" style="text-decoration: none; outline: none;" @click="handleLogoClick()">
          <img src="./assets/companyLogo.jpeg" class="rounded-circle mx-2" width="50" height="50" alt=""><i>Ondeh Ondeh</i>
          </a>
        </router-link>
          <a class="navbar-brand" href="#">
          <img src="./assets/profileIcon.png"  class="rounded-circle" width="50" height="50" alt="">
        </a>
      </div>
    </nav>

    <main>
        <!-- Contains the main content of the webpage-->
      <div>
        <!-- Router View to display components based on routes -->
        <router-view></router-view>
      </div>

    </main>

    <footer>
      <!-- Footer content -->
    </footer>

  </div>
</template>

<script>
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap/dist/js/bootstrap'
  import 'jquery/dist/jquery.min.js'
  import { createRouter, createWebHistory } from 'vue-router'

  export default {
    name: 'App',
    methods: {
      handleLogoClick() {
        try {
          // throw an error to simulate an error occurring
          throw new Error('An error occurred');
        } catch (error) {
          console.error(error);
          // redirect the user back to the LandingPage.vue
          this.$router.push({ name: 'landingPage' });
        }
      }
    },
    router: createRouter(
      {
        history: createWebHistory(process.env.BASE_URL),
        routes: [
          {
            path: "/",
            name: "landingPage",
            component: () => import('../views/LandingPage.vue')
          }
        ]
      }
    )
  }
</script>

<style>
  a{
    text-decoration: none;
  }
  a:hover {
    color: blue;
  }
  .navbar-brand {
      text-decoration: none;
      outline: none;
  }
  a:focus {
    outline: none;
  }
  .navbar {
    background-color: #fff;
  }
  .navbar-brand:hover img {
    transform: scale(1.1);
  }

  .rounded-circle:hover {
    transform: scale(1.1);
  }
  .main-content {
    margin-top: 1rem;
  }
  .rounded-rect {
    border: 2px solid black;
    border-radius: 10px;
  }
  #app {
    font-family: Arial, Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 0px;
  }
</style>