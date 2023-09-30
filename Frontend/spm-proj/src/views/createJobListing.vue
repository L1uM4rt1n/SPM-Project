<template>

    <div class="createJobListing container my-5">
    <div class="text-center">
        <h1 class="">Create Job Listing</h1>
    </div>
    
    <hr>
        <div class="container">
            <div class="form-group">
                <label for="exampleInputEmail1">Name</label>
                <input type="email" class="form-control" id="jobName" aria-describedby="jobName" placeholder="Enter Job Listing Name">
                <!-- <small id="" class="form-text text-muted">This is a small description</small> -->
            </div>

            <label class="my-1 mr-2" for="inlineFormCustomSelectPref">Department</label>
            <select v-model="selectionDepartment" class="custom-select my-1 mr-sm-2 mb-4" id="inlineFormCustomSelectPref">
                <option disabled selected>Choose Department...</option>
                <option v-for="type in jobtypes" :key="type" :value="type">{{ type }}</option>
            </select>
            <br>
            <input  type="text" placeholder="New Deparment">

            <br>
            <label for="exampleFormControlTextarea1">Job Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6"></textarea>

            <!-- Checkboxes -->
            <div class="py-3">
                <label for="Skills">Skills Required</label><br>
                <div v-for="skill in skilltypes" :key="skill" class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" :key="skill" :value="skill">
                    <label class="form-check-label" for="inlineCheckbox1">{{skill}}</label>
                </div>
            </div>


            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>

    


</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

export default {
    name: 'createJobListing',
    // Other component options and code
data() {
        return {
        selectedSkills: [],
        selectedDepartments: [],
        selectedDepartment: '',
        searchKeyword: '', // Add a data property for search keyword
        jobListings: [], // Initialize an empty array for job listings
        jobtypes: [], // All job types
        skilltypes: [], // All skill types
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

        jobListings(newListings) {
            let departmentss = ['New'];
            for (let i = 0; i < newListings.length; i++) {
                let dept = newListings[i].department;
                if (!departmentss.includes(dept)) {
                    departmentss.push(dept);
                }
            }
            this.jobtypes = departmentss;


            let skills = [];
            for (let i = 0; i < newListings.length; i++) {
            skills = skills.concat(newListings[i].skills);
            }

            // Remove duplicates by converting the array to a Set and then back to an array
            this.skilltypes = [...new Set(skills)];
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
        ],
        // Set filteredJobListings to match the initial data
        this.filteredResults = this.jobListings;
      }, 1000); // Simulate an API call delay
    },
    };
</script>



<style>
/* Add your component-specific styles here */
/* .createJobListing {
    text-align: center;
    padding: 20px;
} */

/* Additional styling for elements on this page */
</style>