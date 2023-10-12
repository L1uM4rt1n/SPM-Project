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

                <label class="mr-2" for="inlineFormCustomSelectPref" style="margin-top: 15px;">Availability</label>
                <div>
                    <textarea v-model="NewAvailability" class="form-control" rows="6"></textarea> 
                </div>

            </div>
            
            <div>
                <label for="exampleFormControlTextarea1">Role Description</label>
                <textarea v-model="NewDescription" class="form-control" rows="6"></textarea>
            </div>

            <div>
                <label for="exampleFormControlTextarea1" style="margin-top: 15px;">Role Requirements</label>
                <textarea v-model="NewRequirements" class="form-control" rows="6"></textarea>
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
            TodaysDate: new Date(),

        };
    },
    methods: {
        fetchroles() {
            axios.get("http://127.0.0.1:5000/roles/get_all_roles")
            .then(response => {
                this.filteredResults = response.data.data.bookings
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

            // Create a Date object from the input date string
            const date = new Date(inputDateString);

            // Create an array of day names and month names
            const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
            const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

            // Format the date in the desired format
            const formattedDate = `${dayNames[date.getDay()]} ${monthNames[date.getMonth()]} ${date.getDate()} ${date.getFullYear()}`;

            console.log(inputDateString)
            // Prepare the role data to send in the request body
            const roleData = {
            Role_Name: this.NewRoleName, // Replace with the actual data
            Date_Posted: this.TodaysDate, // Replace with the actual data
            App_Deadline: formattedDate, // Replace with the actual data
            Role_Department: this.NewDepartment, // Replace with the actual data
            Role_Description: this.NewDescription, // Replace with the actual data
            Role_Requirements: this.NewRequirements, // Replace with the actual data

            };

            // Send the PUT request
            axios.put('/roles/create', roleData)
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