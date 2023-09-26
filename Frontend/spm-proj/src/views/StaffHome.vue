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
            </div>
    
            <!-- Display Job Listings -->
            <div class="mb-3" v-for="job in filteredResults" :key="job.id">
            <div class="card border-secondary position-relative">
                <div class="card-body">
                <h4 class="card-title pb-3">{{ job.title }}</h4>
                <p class="card-text">Availability: {{ job.availability }}</p>
                <p class="card-text">Application Deadline: {{ job.deadline }}</p>
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
    name: 'StaffHome',
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
    methods: {
    performSearch(payload) {
        if (payload) {
        const { keyword, selectedDepartments, selectedSkills } = payload;

        // Your filtering logic here based on selected departments, skills, and keyword
        const filteredResults = this.jobListings.filter((job) => {
            const hasSelectedDepartment =
            selectedDepartments.length === 0 ||
            selectedDepartments.includes(job.department);
            const hasSelectedSkills =
            selectedSkills.length === 0 ||
            selectedSkills.some((selectedSkill) =>
                job.skills.includes(selectedSkill)
            );
            const keywordMatch = job.title
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
        this.filteredResults = this.jobListings;
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
    