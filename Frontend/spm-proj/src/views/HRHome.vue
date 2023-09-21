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
            <div class="d-flex flex-row justify-content-between align-items-center p-3">
            <h1 class="mb-0"></h1>
            <router-link :to="{ name: 'createJobListing' }">
                <button class="btn btn-secondary border-dark">Create Job Listing</button>
            </router-link>
            </div>
    
            <!-- Display Job Listings -->
            <div class="mb-3" v-for="job in filteredJobListings" :key="job.id">
            <div class="card border-secondary position-relative">
                <div class="card-body">
                <h4 class="card-title pb-3">{{ job.title }}</h4>
                <p class="card-text">Availability: {{ job.availability }}</p>
                <p class="card-text">Application Deadline: {{ job.deadline }}</p>
                </div>
                <!-- Edit Button (Bottom-right corner) -->
                <div class="position-absolute bottom-0 end-0 m-2 edit-button">
                <a :href="'#edit/' + job.id" class="btn btn-link">Edit</a>
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
        SearchBar,
    },
    data() {
        return {
        selectedSkills: [],
        selectedDepartments: [],
        searchKeyword: '', // Add a data property for search keyword
        jobListings: [], // Initialize an empty array for job listings
        filteredResults:[],
        };
    },
    computed: {
        filteredJobListings() {
      // Your filtering logic here based on selectedSkills, selectedDepartments, and searchKeyword
        return this.jobListings.filter((job) => {
            const hasSelectedSkills =
            this.selectedSkills.length === 0 ||
            this.selectedSkills.some((skill) => job.skills.includes(skill));
            const hasSelectedDepartments =
            this.selectedDepartments.length === 0 ||
            this.selectedDepartments.includes(job.department);
            const keywordMatch = job.title
            .toLowerCase()
            .includes(this.searchKeyword.toLowerCase());

            return hasSelectedSkills && hasSelectedDepartments && keywordMatch;
        });
        },
    },
    methods: {
  performSearch() { // Define the performSearch method
        // Add logs to check variable values
        console.log("performSearch function is executed"); // Log that the function is called
        console.log("searchKeyword:", this.searchKeyword);
        console.log("selectedDepartments:", this.selectedDepartments);
        console.log("selectedSkills:", this.selectedSkills);
        // Filtering logic based on selected department, skills, and keyword
        const filteredResults = this.jobListings.filter((job) => {
        // Check if the job matches selected department
        const hasSelectedDepartment =
            this.selectedDepartments.length === 0 ||
            this.selectedDepartments.includes(job.department);

        // Check if at least one selected skill matches job skills
        const hasSelectedSkills =
            this.selectedSkills.length === 0 ||
            this.selectedSkills.some((selectedSkill) =>
            job.skills.includes(selectedSkill)
            );

        // Check if the keyword is found in the job title (case insensitive)
        const keywordMatch = job.title
            .toLowerCase()
            .includes(this.searchKeyword.toLowerCase());

        // Return true if all criteria match
        return hasSelectedDepartment && hasSelectedSkills && keywordMatch;
        });
        console.log("filteredResults:", filteredResults);

        // Update the jobListings array with the filtered results
        this.jobListings = filteredResults;
        console.log("jobListings after filtering:", this.jobListings);
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
            this.jobListings = [
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
        this.filteredJobListings = this.jobListings;
      }, 1000); // Simulate an API call delay
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
</style>
    