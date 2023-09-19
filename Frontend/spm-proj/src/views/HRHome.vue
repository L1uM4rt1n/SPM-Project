<template>
    <div class="container">

        <!-- Search Bar -->
        <SearchBar/>


        <div class="container">
        <!-- Your Bootstrap job listings/cards here -->
            <div class="container"> <!-- Display Ttile and Creating listing button -->

                <h1 class="text-center">Job Listings</h1>

                <div class="d-flex flex-row justify-content-end p-1">

                    <!-- Create Job Listing Button -->
                    <router-link :to="{ name: 'createJobListing' }">
                        <a class="btn btn-primary" href="#" role="button">Create Job Listing</a>
                    </router-link>
                
                </div>

            </div>


            <div class=""> <!-- Container containing cards -->
                <div class="card"> <!-- Card Listing -->
                    <div class="card-body">
                        <h5 class="card-title">Software Developer</h5>
                        <p class="card-text">Skills: You need to be able to code.</p>
                        <div class="d-flex justify-content-end mb-auto float">
                            <a href="#" class="btn">Edit</a>
                        </div>
                    </div>
                </div> 
            </div>



        </div>
    </div>

</template>

<script>
import SearchBar from '../components/SearchBar.vue';
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

export default {
    name: 'HRHome',
    components: {
        SearchBar
    }
};
</script>



<style>

</style>