<template>

    <div class="createJobListing container my-5">
    <div class="text-center">
        <h1 class="">Create Role Listing</h1>
    </div>
    
    <hr>
        <div class="container">
            <div class="form-group">
                <label for="exampleInputEmail1">Name</label>
                <input type="email" class="form-control" id="jobName" aria-describedby="jobName" placeholder="Enter Role Listing Name" style="margin-bottom: 15px;">
                <!-- <small id="" class="form-text text-muted">This is a small description</small> -->
            </div>


            <div>
                Application Deadline <br>
                <input type="date" id="myDate" value="2023-10-09">

            </div>

            <div>
                <label class="mr-2" for="inlineFormCustomSelectPref" style="margin-top: 15px;">Department</label>
                <div>
                    <select v-model="selectedDepartments" class="custom-select my-1 mr-sm-2 mb-4" id="inlineFormCustomSelectPref">
                        <option disabled selected>Choose Department...</option>
                        <option>New</option>
                        <option v-for="job in filteredResults" :key="job" :value="job">{{ job.Role_Department }}</option>
                    </select>
                </div>

                <input v-if="selectedDepartments === 'New'" type="text" placeholder="New Department Name" style="width: 100%;">
            </div>
            
            <div>
                <label for="exampleFormControlTextarea1">Role Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6"></textarea>
            </div>

            <div>
                <label for="exampleFormControlTextarea1" style="margin-top: 15px;">Role Expectations</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6"></textarea>
            </div>

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

        </div>
    </div>

    


</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS
import axios from 'axios';

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
        jobListings: {}, // Initialize an empty array for job listings
        jobtypes: [], // All job types
        skilltypes: [], // All skill types
        filteredResults:[],
        };
    },
    methods: {
        fetchroles() {
            axios.get("http://127.0.0.1:5000/roles/get_all_roles")
            .then(response => {
                this.filteredResults = response.data.data.bookings
                //console.log('----FilteredResults-----')
                //console.log(this.filteredResults)


                for(let i = 0; i < this.filteredResults.length; i++){
                    //console.log(this.filteredResults[i])
                    this.jobListings[i] = this.filteredResults[i]
                }

                //console.log('----jobListing-----')
                //console.log(this.jobListings[0])

                let departmentss = ['New'];
                for (let i = 0; i < this.jobListings.length; i++) {
                    let dept = this.jobListings[i].Role_Department;
                    console.log('1');
                    if (!departmentss.includes(dept)) {
                        departmentss.push(dept);
                }

                this.jobtypes = departmentss;

                console.log(this.jobtypes)
            }
                

            })
            .catch(error => {
                console.error("There was an error fetching the data:", error);
            });
        },
        populating() {
            let departmentss = ['New'];
            console.log(this.jobListings)
            for (let i = 0; i < this.jobListings.length; i++) {
                let dept = this.jobListings[i].Role_Department;
                console.log('1');
                if (!departmentss.includes(dept)) {
                    departmentss.push(dept);
                }
            }
            this.jobtypes = departmentss;


            let skills = [];
            for (let i = 0; i < this.jobListings.length; i++) {
            skills = skills.concat(this.jobListings[i].skills);
            }

            // Remove duplicates by converting the array to a Set and then back to an array
            this.skilltypes = [...new Set(skills)];
            },
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
        // Use axios to fetch data from Flask API
        this.fetchroles();
        this.populating();
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