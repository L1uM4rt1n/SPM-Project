<template>
    <div class="container">
        <!-- Search Bar -->
        <SearchBar
            v-model="searchKeyword"
            :selectedSkills="selectedSkills"
            :selectedDepartments="selectedDepartments"
            @search-request="performSearch"
        />
    
        <div class="container">
            <!-- Display Title and Create Listing Button -->
            <div class="d-flex flex-row justify-content-between align-items-center">
            <h1 class="mb-0"></h1>
            <!-- <router-link :to="{ name: 'createJobListing' }"> -->
                <button class="btn btn-secondary border-dark my-2">Create Job Listing</button>
            <!-- </router-link> -->
            </div>

            <!-- Display Job Listings -->
            <div class="mb-1" v-for="role in filteredResults" :key="role.role_ID">
            <div class="card border-secondary position-relative">
                <div class="card-body">
                    <h4 class="card-title">{{ role.Role_Name }} <span class="text-secondary border border-rounded">(Available: {{role.Availability}})</span></h4>
                    <p class="card-text">Role ID: {{  role.Role_ID }}</p>
                    <p class="card-text">Department: {{ role.Role_Department }}</p>
                    <p class="card-text">Application Deadline: {{ formatDateWithoutTime(role.App_Deadline) }}</p>
                </div>
                <!-- Edit Button (Bottom-right corner) -->
                <div class="position-absolute bottom-0 end-0 m-2 edit-button">
                <a :href="'#edit/' + role.id" class="btn btn-link" style="text-decoration: none;">Edit</a>
                </div>
            </div>
            </div>
        </div>
    </div>
    </template>
    
<script>
import SearchBar from '../../components/SearchBar.vue';
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 5 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 5 JS
import axios from 'axios';


    export default {
    name: 'HRHome',
    components: {
        SearchBar,
    },
    data() {
        return {
        selectedSkills: [],
        selectedDepartments: [],
        searchKeyword: '', // Add a data property for search keyword
        roleListings: [], // Initialize an empty array for role listings for role objects
        filteredResults:[],
        departments:[],
        skills:[],
        Email:'',
        Access:'',
        };
    },
    methods: {
        performSearch(payload) {
            if (payload) {
                const { keyword, selectedDepartments, selectedSkills } = payload;

                // Filter the role listings based on selected departments, skills, and keyword
                const filteredResults = this.roleListings.filter((role) => {
                    const hasSelectedDepartment =
                        selectedDepartments.length === 0 ||
                        selectedDepartments.includes(role.Role_Department);

                    const hasSelectedSkills =
                        selectedSkills.length === 0 ||
                        selectedSkills.some((selectedSkill) =>
                            role.Role_Skills.includes(selectedSkill)
                        );

                    // Check for a keyword match in both the role name and description
                    const keywordMatch =
                    (role.Role_Name &&
                        role.Role_Name.toLowerCase().includes(keyword.toLowerCase())) ||
                    (role.Role_Description &&
                        role.Role_Description.toLowerCase().includes(keyword.toLowerCase()));


                    return hasSelectedDepartment && hasSelectedSkills && keywordMatch;
                });

                this.filteredResults = filteredResults;
            }
        },
        getDeadlineYear(deadline){
            const date = new Date(deadline);
            const year = date.getFullYear();
            return date.toDateString().replace(/\d{4}$/,year)
        },
        formatDateWithoutTime(dateString) {
            const date = new Date(dateString);
            const options = { weekday: 'short', day: '2-digit', month: 'short', year: 'numeric' };
            return date.toLocaleDateString('en-US', options);
        },

    },

    watch: {
        // Watch for changes to the searchKeyword and trigger performSearch
        searchKeyword: function() {
            this.performSearch(); // Call the performSearch method when searchKeyword changes
        },
    },
    created() {
        // Retrieve the email and access rights from sessionStorage
        this.Email = sessionStorage.getItem('Email');
        this.Access = sessionStorage.getItem('Access');

        console.log("===== Email and access stored in Session =====")
        console.log("Email:" + this.Email + " == Access:" + this.Access)


        // Make an HTTP GET request to the '/roles/get_all_roles' endpoint
        axios.get('http://localhost:5008/roles/get_all_roles')
            .then((response) => {
            // Check for a successful response (status code 200)
            if (response.status === 200) {
                // Assuming the data returned is in response.data.data.bookings
                console.log("============= response.data in HRHome.vue ===========")
                console.log(response.data)
                this.roleListings = response.data.data.roles_with_details;
                console.log("============= roleListings in HRHome.vue ============")
                console.log(this.roleListings)
                // Filter the roleListings based on the application deadline
                const today = new Date();
                this.roleListings = this.roleListings.filter((role) => {
                    const deadline = new Date(role.App_Deadline);
                    return deadline > today;
                });
                this.filteredResults = this.roleListings;
            }
            })
            .catch((error) => {
            // Handle any errors or show a message to the user
            console.error('Error fetching data:', error);
            });
    },
    };
</script>

<style>
/* Custom CSS for the Edit button */
.edit-button {
    position: absolute;
    bottom: 0;
    right: 0;
    margin: 10px; /* Adjust margin as needed */
}

.scrollable-menu {
    max-height: 300px; /* Adjust the maximum height as needed */
    overflow-y: auto;
}

</style>
    