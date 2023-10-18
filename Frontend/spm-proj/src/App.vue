<template>
  <div id="app">

    <!-- header content -->
    <header>

    </header>
    
    <!-- navBar -->
    <nav class="navbar navbar-light navbar-expand-lg border-bottom border-dark">
      <div class="container-fluid">
        <router-link :to="{ name: 'landingPage' }">
          <a class="navbar-brand btn" href="#" style="text-decoration: none; outline: none;">
            <img src="./assets/companyLogo.jpeg" class="mx-2 rounded" width="120" height="80" alt="">
            <i>Ondeh Ondeh</i>
          </a>
        </router-link>

          <a class="navbar-brand" href="#">
          <router-link :to="{ name: 'Profile'}">
            <img src="./assets/profileIcon.png"  class="rounded-circle" width="50" height="50" alt="">
          </router-link>
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

  export default {
    name: 'App',
    methods: {
    },
    router: createRouter(
      {
        history: createWebHistory(process.env.BASE_URL),
        routes: [
          {
            path: "/",
            name: "landingPage",
            component: () => import('./views/LandingPage.vue')
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
