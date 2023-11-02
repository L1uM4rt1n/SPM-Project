<template>
  <div id="app">

    <!-- header content -->
    <header>
    </header>
    
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom border-dark">
      <div class="container-fluid">
        <router-link :to="{ name: 'landingPage' }">
          <a class="navbar-brand btn" href="#" style="text-decoration: none; outline: none;">
            <img src="./assets/companyLogo.jpeg" class="mx-2 rounded img-fluid logo-img" alt="">
            <i>Ondeh Ondeh</i>
          </a>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarNav">
          <ul class="navbar-nav">
            <!-- You can add other navigation links here -->
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#"><img src="./assets/profileIcon.png" class="rounded-circle img-fluid profile-img" width="50" height="50" alt=""></a>
            </li>
          </ul>
        </div>
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
  .logo-img {
  width: 120px; /* Default size */
}

.profile-img {
  width: 50px; /* Default size */
}

@media (max-width: 768px) {
  .logo-img {
    width: 100px; /* Adjust size for medium screens */
  }

  .profile-img {
    width: 40px; /* Adjust size for medium screens */
  }
}

@media (max-width: 576px) {
  .logo-img {
    width: 80px; /* Adjust size for small screens */
  }

  .profile-img {
    width: 30px; /* Adjust size for small screens */
  }
}
</style>
