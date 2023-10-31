<template>
    <div class="landing-page">
      <div class="background-image">
        <div class="content">
          <h1 class="text-white" style="font-weight: bold;  font-size: 55px;">All-in-One Learning Management System</h1>
          <p class="text-white">This is an all-in-one system where you can view and manage your role listing.</p>
          <!-- Login Button -->
          <router-link :to="{ name: 'LoginPage' }">
            <a class="btn btn-lg btn-light border-light mt-3 px-5" href="#" role="button">Login</a>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  
  
  <script>
    import 'bootstrap/dist/css/bootstrap.css'
    import 'jquery/dist/jquery.min.js'
    import 'bootstrap/dist/js/bootstrap.min.js'
    
    export default {
          methods: {
          },
          mounted() {
                document.title = "SBRP Portal";
          },
          name: 'landingPage'
    }
  </script>
  
  <style>
    .landing-page {
      background-color: #0a74da;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    .background-image {
      background-image: url('../assets/LandingBackground.jpeg');
      background-size: cover;
      background-position: center center;
      width: 100%;
      height: 100%;
      position: relative;
      opacity: 0.8;
    }
  
    .content {
      text-align: center;
      padding: 20px;
      background-color: rgba(75, 75, 75, 0.6);
      border-radius: 10px;
    }
  
    .text-white {
      color: #fff;
        margin: 0;
    }
  </style>