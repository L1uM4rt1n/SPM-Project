<template>
    <div class="landing-page">
        <h1>Welcome to the Landing Page</h1>
        <div class="container mx-auto">
            
            <!-- Add your page content here -->
            <div class="d-flex flex-row justify-content-center p-1">

                <!-- HR Home Button -->
                <router-link :to="{ name: 'HRHome' }">
                    <a class="btn btn-primary" href="#" role="button">To HR Home Page</a>
                </router-link>

                <!-- Staff Home Button -->
                <!-- <router-link :to="{ name: 'StaffHome' }">
                    <a class="btn btn-primary" href="#" role="button">Create Job Listing</a>
                </router-link> -->


            </div>
        </div>

    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

export default {
name: 'landingPage',
// Other component options and code
};
</script>

<style>
/* Add your component-specific styles here */
.new-page {
text-align: center;
padding: 20px;
}

/* Additional styling for elements on this page */
</style>
