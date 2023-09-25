<template>
      <div class="landing-page">
            <h1 class="page-title m-5"> Welcome to Ondeh Ondeh SBRP Portal </h1>
            
            <div class="container mx-auto">
                  <!-- HR Home Page -->
                  <div class="jumbotron">
                        <p class="lead">
                              <!-- HR Home Button -->
                              <button class="btn-lg btn-secondary border-dark w-30" @click="goToHRHome">
                                    To HR Home Page
                              </button>
                  </p>
                  </div>

                  <!-- Staff Home Page -->
                  <div class="jumbotron">
                        <p class="lead">
                              <!-- Staff Home Button -->
                              <button class="btn-lg btn-secondary border-dark w-30" @click="goToStaffHome">
                                    To Staff Home Page
                              </button>
                        </p>
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
                  goToHRHome() {
                        this.$router
                              .push({ name: 'HRHome' })
                              .catch((error) => {
                                    console.error("Error navigating to HR Home Page:", error);
                                    this.$router.push({ name: "landingPage" });
                              });
                  },
                  goToStaffHome() {
                        this.$router
                              .push({ name: 'StaffHome' })
                              .catch((error) => {
                                    console.error("Error navigating to Staff Home Page:", error);
                                    this.$router.push({ name: "landingPage" });
                              });
                  }
            },
            mounted() {
                  document.title = "SBRP Portal";
            },
            name: 'landingPage'
            
            // created funtion to test if routing works
            // created() {
            //       console.log('LandingPage created');
            // }
      };
</script>

<style>
      .new-page {
      text-align: center;
      padding: 20px;
      }
      .page-title {
            font-size: 3rem;
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 2rem;
            color: #2e7166;
      }
      .btn-lg {
            font-size: 1.5rem;
            padding: 1rem 2rem;
            border-radius: 2rem;
            transition: all 0.3s ease-in-out;
      }

      .btn-lg:hover {
            transform: scale(1.1);
      }

      .border-dark {
            border-color: #2e7166;
      }

      .border-dark:hover {
            border-color: #1a4731;
      }
</style>
