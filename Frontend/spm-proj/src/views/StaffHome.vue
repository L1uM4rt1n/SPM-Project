<template>
    <div class="container">
        <!-- Search Bar -->
        <SearchBar
                v-model="searchKeyword"
                :selectedSkills="selectedSkills"
                :selectedDepartments="selectedDepartments"
                @search-request="performSearch"
        />
    
        <!-- Display Job Listings -->
        <div class="container">
            <router-link to="'/role/' + role.slug" class="card-link" v-for="role in filteredResults" :key="role.id">
                <div class="card">
                    <div class="card-body">
                        <h4 class="card-title">{{ role.title }}</h4>
                        <h6 class="card-text">Role ID: {{  role.id }}</h6>
                        <p class="card-text">Availability: {{ role.availability }}</p>
                        <p class="card-text">Application Deadline: {{ role.deadline }}</p>
                    </div>
                </div>
            </router-link>
        </div>
    </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue';
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

    export default{
        name: 'StaffPage',
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
          // Add more role listings here
        ];
        // Set filteredJobListings to match the initial data
        this.filteredResults = this.roleListings;
      }, 1000); // Simulate an API call delay
    },

    }

</script>

<style>
    .circle{
        width: 10px;
        height: auto;
        border-radius: 50%;
        text-align: center;
    }

    .card-link{
        text-decoration: none;
    }

</style>

