<template>

    <div class="createJobListing container my-5">
    <div class="text-center">
        <h1 class="">Create Role Listing</h1>
    </div>
    
    <hr>
        <div class="container">
            <div class="form-group">
                <label for="exampleInputEmail1">Name</label>
                <input type="email" class="form-control" id="jobName" aria-describedby="jobName" placeholder="Enter Job Listing Name" style="margin-bottom: 15px;">
                <!-- <small id="" class="form-text text-muted">This is a small description</small> -->
            </div>

            <div class="form-group">
                <label for="exampleInputEmail1" style="margin-right: 10px;">Application Deadline</label>

                <!-- Day dropdown -->
                <select v-model="selectedDay" style="width: 100px; margin-right: 5px;" >
                    <option disabled selected>DD</option>
                    <option v-for="day in 31" :key="day" :value="day">{{ day }}</option>
                </select>
                /

                <!-- Month dropdown -->
                <select v-model="selectedMonth" style="width: 100px; margin-right: 5px;">
                    <option disabled selected>MM</option>
                    <option v-for="month in 12" :key="month" :value="month">{{ month }}</option>
                </select>
                /
                <!-- Year dropdown -->
                <select v-model="selectedYear" style="width: 100px; margin-right: 5px;">
                    <option disabled selected>YYYY</option>
                    <option v-for="year in 9" :key="year" :value="year + 2022">{{ year + 2022 }}</option>
                </select>
            </div>



            <label class="my-1 mr-2" for="inlineFormCustomSelectPref">Department</label>
            <div>
                <select v-model="selectedDepartments" class="custom-select my-1 mr-sm-2 mb-4" id="inlineFormCustomSelectPref">
                    <option disabled selected>Choose Department...</option>
                    <option v-for="type in jobtypes" :key="type" :value="type">{{ type }}</option>
                </select>
            </div>

            <input v-if="selectedDepartments === 'New'" type="text" placeholder="New Department Name" style="width: 100%;">

            <br>
            <label for="exampleFormControlTextarea1">Role Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6"></textarea>

            <!-- Checkboxes -->
            <div class="py-3">
                <label for="Skills">Skills Required</label><br>
                <div v-for="skill in skilltypes" :key="skill" class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" :key="skill" :value="skill">
                    <label class="form-check-label" for="inlineCheckbox1">{{skill}}</label>
                </div>
                    
                <!-- Additional 'Other' checkbox -->
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="otherSkill" v-model="isOtherChecked">
                    <label class="form-check-label" for="otherSkill">Other</label>
                </div>
            </div>
            <br>
            <textarea v-if="isOtherChecked" placeholder="Please specify the other skill(s)" style="width: 100%;"></textarea>
            <br>
            <router-link :to="{ name: 'createSuccess' }">
                <button type="submit" class="btn btn-primary">Submit</button>
            </router-link>
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
        checkedSkills: [],  // This will store checked skills
        isOtherChecked: false,  // This will track if 'Other' is checked
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