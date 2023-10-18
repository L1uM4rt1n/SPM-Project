<template>

    <div class="createJobListing container my-5">
    <div class="text-center">
        <h1 class="">Create Role Listing</h1>
    </div>
    
    <hr>
        <div class="container">
            <div class="form-group">
                <label for="exampleInputEmail1">Name</label>
                <input v-model="NewRoleName" type="email" class="form-control" id="jobName" aria-describedby="jobName" placeholder="Enter Role Listing Name" style="margin-bottom: 15px;">
                <!-- <small id="" class="form-text text-muted">This is a small description</small> -->
            </div>

            <div>
                Application Deadline <br>
                <input v-model="NewDeadline" type="date" id="myDate">

            </div>

            <div>
                <label class="mr-2" for="inlineFormCustomSelectPref" style="margin-top: 15px;">Department</label>
                <div>
                    <select v-model="NewDepartment" class="custom-select my-1 mr-sm-2 mb-4" id="inlineFormCustomSelectPref">
                        <option disabled selected>Choose Department...</option>
                        <option v-for="job in filteredResults" :key="job" :value="job.Role_Department">{{ job.Role_Department }}</option>
                    </select>
                </div>

                
                <div>
                    <label for="inlineFormCustomSelectPref" style="margin-top: 15px;">Availability</label>
                    <textarea v-model="NewAvailability" class="form-control" ></textarea> 
                </div>

            </div>
            
            <div>
                <label for="exampleFormControlTextarea1">Role Description</label>
                <textarea v-model="NewDescription" class="form-control" rows="6" ></textarea>
            </div>

            <div>
                <label for="exampleFormControlTextarea1" style="margin-top: 15px;">Role Requirements</label>
                <textarea v-model="NewRequirements" class="form-control" rows="6" ></textarea>
            </div>

            <div>
                <label for="exampleFormControlTextarea1" style="margin-top: 15px;" >Role Skills</label>
                <textarea v-model="NewRoleSkills" class="form-control" rows="6" placeholder='Enter All Skills, Each Seperated By A Comma' style='text-align:center'></textarea>
            </div>

            <br>
            <button class="btn btn-success" v-on:click="createrole">Create</button>

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
            filteredResults:[], //response.data.data.bookings is here
            searchKeyword: '', // Add a data property for search keyword
            NewRoleName: '', // the new role name
            NewDepartment: '', //the new department
            NewDescription: '', // the new Role Description
            NewRequirements: '', // the new Role Requirements
            NewDeadline: '', // the new Deadline
            NewAvailability: '', // the avaiability for new role
            NewRoleSkills: '', // the skills for the new role

        };
    },
    methods: {
        fetchroles() {
            axios.get("http://127.0.0.1:5000/roles/get_all_roles")
            .then(response => {
                this.filteredResults = response.data.data.roles_with_details
                console.log(this.filteredResults)
            })
            .catch(error => {
                console.error("There was an error fetching the data:", error);
            });
        },
        test() {
            console.log(this.NewDeadline)
            console.log(this.NewDepartment)
            console.log(this.NewDescription)
            console.log(this.NewRequirements)
            console.log(this.NewRoleName)
            console.log(this.TodaysDate)
        },
        createrole() {
            const inputDateString = this.NewDeadline
            
            // Get the current date
            const today = new Date();

            // Get the year, month, and day components
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
            const day = String(today.getDate()).padStart(2, '0');

            // Format the date as YYYY-MM-DD
            const formattedDateToday = `${year}-${month}-${day}`;

            const formattedSkills = this.NewRoleSkills.split(','); 
 

            // Prepare the role data to send in the request body
            const roleData = {
            Role_Name: this.NewRoleName,
            Date_Posted: formattedDateToday,
            App_Deadline: inputDateString,
            Role_Department: this.NewDepartment, 
            Role_Description: this.NewDescription, 
            Role_Requirements: this.NewRequirements,
            Availability: this.NewAvailability,
            Role_Skills: formattedSkills

            };

            // Send the PUT request
            axios.post('http://127.0.0.1:5000/role/create', roleData)
            .then(response => {
                // Handle the successful response here
                console.log('Role created:', response.data);
            })
            .catch(error => {
                // Handle any errors here
                console.error('Error creating role:', error);
            });
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