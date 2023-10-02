<template>
    <div class="container">
        <!-- Search Bar -->
        <SearchBar
            v-model:keywordSearch="searchKeyword"
            :selectedSkills="selectedSkills"
            :selectedDepartments="selectedDepartments"
            @search-request="performSearch"
        />
    
        <div class="container">
            <!-- Display Title and Create Listing Button -->
            <div class="d-flex flex-row justify-content-between align-items-center p-2">
            <h1 class="mb-0"></h1>
            <!-- <router-link :to="{ name: 'createJobListing' }"> -->
                <button class="btn btn-secondary border-dark">Create Job Listing</button>
            <!-- </router-link> -->
            </div>

            <!-- Display Job Listings -->
            <div class="mb-3" v-for="role in filteredResults" :key="role.id">
            <div class="card border-secondary position-relative">
                <div class="card-body m-2">
                <h4 class="card-title pb-3">{{ role.title }}</h4>
                <p class="card-text">Role ID: {{  role.id }}</p>
                <p class="card-text">Availability: {{ role.availability }}</p>
                <p class="card-text">Application Deadline: {{ role.deadline }}</p>
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
import SearchBar from '../components/SearchBar.vue';
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS
// import axios from 'axios';


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
        roleListings: [], // Initialize an empty array for job listings
        filteredResults:[],
        };
    },
    methods: {
    performSearch(payload) {
        if (payload) {
        const { keyword, selectedDepartments, selectedSkills } = payload;

        // Your filtering logic here based on selected departments, skills, and keyword
        const filteredResults = this.roleListings.filter((role) => {
            const hasSelectedDepartment =
            selectedDepartments.length === 0 ||
            selectedDepartments.includes(role.department);
            const hasSelectedSkills =
            selectedSkills.length === 0 ||
            selectedSkills.some((selectedSkill) =>
                role.skills.includes(selectedSkill)
            );
            const keywordMatch = role.title
            .toLowerCase()
            .includes(keyword.toLowerCase());

            return hasSelectedDepartment && hasSelectedSkills && keywordMatch;
        });
        this.filteredResults = filteredResults;
        }
        },
    },

    watch: {
        // Watch for changes to the searchKeyword and trigger performSearch
        searchKeyword: function() {
            this.performSearch(); // Call the performSearch method when searchKeyword changes
        },
    },
    mounted() {
      // Simulate fetching data from a database (replace with actual data fetching)
        setTimeout(() => {
            this.roleListings = [
            {
            id: 1,
            title: 'Software Developer',
            skills: ['Java', 'HTML'],
            department: 'IT',
            availability: 2,
            deadline: '31/09/2002',
            },
            {
            id: 2,
            title: 'Frontend Developer',
            skills: ['HTML', 'CSS', 'JavaScript'],
            department: 'HR',
            availability: 2,
            deadline: '26/09/2002',
            },
          // Add more job listings here
        ];
        // Set filteredJobListings to match the initial data
        this.filteredResults = this.roleListings;
      }, 200); // Simulate an API call delay
    },
    };
    
    //     mounted() {
    //     // Make an Axios GET request to fetch role listings from your SQL database
    //     axios.get('your-api-endpoint-here')
    //         .then((response) => {
    //             // Assuming your API response contains role listings in response.data
    //             this.roleListings = response.data;

    //             // Set filteredResults to match the initial data
    //             this.filteredResults = this.roleListings;
    //         })
    //         .catch((error) => {
    //             console.error('Error fetching data:', error);
    //         });
    // },
</script>

<style>
/* Custom CSS for the Edit button */
.edit-button {
    position: absolute;
    bottom: 0;
    right: 0;
    margin: 10px; /* Adjust margin as needed */
}
</style>
    