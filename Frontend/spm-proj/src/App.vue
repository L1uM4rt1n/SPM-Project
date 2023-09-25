<template>
  <div id="app">

    <!-- header content -->
    <header>

    </header>
    
    <!-- navBar -->
    <nav class="navbar navbar-light navbar-expand-lg border-bottom border-dark">
      <div class="container-fluid">
        
        <!-- landing page -->
        <router-link :to="{ name : 'landingPage'}">
          <a href="./App.vue" class="navbar-brand text-decoration-none">
            <img src="./assets/companyLogo.jpeg" 
                  class="rounded-rect" 
                  width="120" 
                  height="80"
                  alt="">
            <!-- <i> Ondeh Ondeh </i> -->
          </a>
        </router-link>

        <!-- personal profile icon -->
        <a href="#" class="navbar-brand ml-auto">
          <img src="./assets/profileIcon.png" 
                alt="" 
                class="rounded-circle"
                width="50"
                height="50">
        </a>
      </div>
    </nav>

    <hr class="my-0">

    <main>
      <div>
        <!-- rendering component based on current route -->
        <router-view></router-view>
      </div>
    </main>

  </div>
</template>

<script>
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap/dist/js/bootstrap'
  import 'jquery/dist/jquery.min.js'
  import { createRouter, createWebHistory } from 'vue-router'
  import landingPage from './views/LandingPage.vue'

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
            component: landingPage
          }
        ]
      }
    )
  }
</script>

<style>
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
