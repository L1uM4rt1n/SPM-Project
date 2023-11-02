<template>

    <div class="createJobListing container my-5">
    <div class="text-center">
        <h1 class="">Create Role Listing</h1>
    </div>
    <router-link to="/hr-home">
      <button class="btn btn-light top-left-button">Back</button>
    </router-link>
    
    <hr>
        <div class="container" style="text-align: left;">
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
                        <option v-for="job in filteredResults2" :key="job" :value="job">{{ job }}</option>
                    </select>
                </div>

            </div>
            
            <div>
                <label for="exampleFormControlTextarea1">Role Description</label>
                <textarea v-model="NewDescription" class="form-control" rows="6" ></textarea>
            </div>

        <div>
            <label for="exampleFormControlTextarea1" style="margin-top: 15px;">Role Skills</label>
            <br>
            <label for="allSkills">Select Skill</label>
            <select v-model="selectedSkill" @change="addSkillToSelectedSkills">
                <option value="">Select a skill</option>
                <option v-for="skill in allskills" :key="skill" :value="skill">{{ skill }}</option>
            </select>
        </div>

        <div class="checkboxes">
            <label v-for="addedskill in selectedSkills" :key="addedskill">
                <input type="checkbox" :value="addedskill" v-model="selectedSkills"> {{ addedskill }}
            </label>
        </div>
        {{selectedSkills}}

            <br>
            <button class="btn btn-success" v-on:click="createrole">Create</button>

        </div>
    </div>

    


</template>

<script>
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.min.js'
import 'jquery/dist/jquery.min.js';
import axios from 'axios';
import { server } from "../../utils/helper.js";

export default {
  name: 'createJobListing',
  data() {
    return {
      filteredResults: [],
      filteredResults2: [],
      allskills: [],
      NewRoleName: '',
      NewDepartment: '',
      NewDescription: '',
      NewDeadline: '',
      NewRoleSkills: '',
      FinalSkills: [],
      selectedskill: "",
      selectedSkills:[],
    };
  },
  methods: {
    fetchroles() {
      axios.get(`${server.baseURL}/roles/get_all_roles`)
        .then(response => {
          this.filteredResults = response.data.data.roles_with_details;
          for (const job of this.filteredResults) {
            if (!this.filteredResults2.includes(job.Role_Department)) {
                this.filteredResults2.push(job.Role_Department);
            }
          }
          console.log(this.filteredResults);
        })
        .catch(error => {
          console.error("There was an error fetching the data:", error);
        });
    },
     addSkillToSelectedSkills() {
      if (this.selectedSkill) {
        this.selectedSkills.push(this.selectedSkill);
        this.selectedSkill = ""; // Reset the selected skill
      }
    },
    fetchskills() {
      axios.get(`${server.baseURL}/skills/get_all_skills`)
        .then(response => {
          this.allskills = response.data.data.skill_names;
          console.log(this.allskills);
        })
        .catch(error => {
          console.error("There was an error fetching the data:", error);
        });
    },
     test() {
      console.log(this.NewDeadline);
      console.log(this.NewDepartment);
      console.log(this.NewDescription);
      console.log(this.NewRoleName);
    },
    addSelectedSkills() {
      // Perform any action with the selected skills, for example, you can add them to another array or perform an API call.
      this.FinalSkills.push(this.selectedSkills[0])
      console.log('Selected Skills:', this.FinalSkills);

    },
    createrole() {
      const inputDateString = this.NewDeadline;

      // Get the current date
      const today = new Date();

      // Get the year, month, and day components
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
      const day = String(today.getDate()).padStart(2, '0');

      // Format the date as YYYY-MM-DD
      const formattedDateToday = `${year}-${month}-${day}`;

      // Prepare the role data to send in the request body
      const roleData = {
        Role_Name: this.NewRoleName,
        Role_Department: this.NewDepartment,
        Date_Posted: formattedDateToday,
        App_Deadline: inputDateString,
        Role_Description: this.NewDescription,
        Role_Skills: this.selectedSkills,
      };

      // Send the POST request to create a role
      axios.post(`${server.baseURL}/role/create`, roleData)
        .then(response => {
          // Handle the successful response here
          console.log('Role created:', response.data);
        })
        .catch(error => {
          // Handle any errors here
          console.error('Error creating role:', error);
        });
    },
  },
  mounted() {
    // Use axios to fetch data from Flask API
    this.fetchroles();
    this.fetchskills();
  },
};
</script>




<style>
/* Add your component-specific styles here */
/* .createJobListing {
    text-align: center;
    padding: 20px;
} */
.top-left-button {
  background-color: #f0f0f0;
  color: #333;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  position: absolute;
  top: /* Height of your navbar */ 150px;
  left: 30px; /* Adjust this value to control the horizontal position */
  z-index: 1; /* Ensures the button is above other content */
}
/* Additional styling for elements on this page */
</style>