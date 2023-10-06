<template>
    <div class="landing-page">
        <h1 class="m-5">Welcome to the Landing Page</h1>
        <div class="container mx-auto">
            <div class="border p-5  my-3 bg-light rounded">
                <h1 class="display-4">HR Home!</h1>
                <hr class="my-4">
                <p class="lead">
                    <!-- HR Home Button -->
                    <router-link :to="{ name: 'HRHome' }">
                        <a class=" btn btn-lg btn-secondary border-dark" href="#" role="button">To HR Home Page</a>
                    </router-link>
                </p>
            </div>
            <div class="border p-5  my-3 bg-light rounded">
                <h1 class="display-4">Staff Home!</h1>
                <hr class="my-4">

                <p class="lead">
                    <!-- HR Home Button -->
                    <router-link :to="{ name: 'StaffPage' }">
                        <a class=" btn btn-lg btn-secondary border-dark" href="#" role="button">To Staff Home Page</a>
                    </router-link>
                </p>
                </div>
        </div>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; 
import 'jquery/dist/jquery.min.js'; 
import 'bootstrap/dist/js/bootstrap.min.js'; 

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