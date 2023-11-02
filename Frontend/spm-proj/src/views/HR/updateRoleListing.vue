<template>

    <div class="updateRoleListing container my-5">
    <div class="text-center">
        <h1 class="">Update Role Listing</h1>
        <p>Role ID: {{ $route.params.roleId }}</p>
    </div>
    <router-link to="/hr-home">
      <button class="btn btn-light top-left-button">Back</button>
    </router-link>
    
    <hr>
        <div class="container" style="text-align: left;">
            <div class="form-group">
                <label>Name</label>
                <input type="text" class="form-control" id="jobName" aria-describedby="jobName" style="margin-bottom: 15px;" v-model="roleData.Role_Name">
            </div>


            <div>
                Application Deadline <br>
                <input type="date" class="form-control" id="myDate" v-model="formattedDate"> 

            </div>

            <div>
                <label class="mr-2" for="inlineFormCustomSelectPref" style="margin-top: 15px;">Department</label>
                <div>
                    <select class="custom-select my-1 mr-sm-2 mb-4" id="inlineFormCustomSelectPref">
                        <option disabled selected>Choose Department...</option>
                        <option v-for="job in filteredResults" :key="job" :value="job.Role_Department" :selected="job.Role_Department == roleData.Role_Department">{{ job.Role_Department }}</option>
                    </select>
                </div>

            </div>
            
            <div>
                <label for="exampleFormControlTextarea1">Role Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6" v-model="roleData.Role_Description"></textarea>
            </div>


            <!-- Checkboxes -->
            <div class="py-3">
                <label for="Skills">Skills Required</label><br>
                <div v-for="skill in roleData.Role_Skills" :key="skill" class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" :key="skill" :value="skill" @change="updateRoleSkills(skill)" checked>
                    <label class="form-check-label" for="inlineCheckbox1">{{skill}}</label>
                </div>
                    
            <div>
            <br>
            <label for="allSkills">Add Skill</label>
            <select v-model="selectedSkill" @change="addSkillToSelectedSkills">
                <option value="">Select a skill</option>
                <option v-for="skill in allskills" :key="skill" :value="skill">{{ skill }}</option>
            </select>
            </div>

            </div>
            <br>
                <textarea v-if="isOtherChecked" placeholder="Please specify the other skill(s)" style="width: 100%;"></textarea>
            <br>

            <button class="btn btn-secondary" type="submit" @click="submitChanges() ">Save Changes</button>
        </div>
    </div>

    


</template>

<script>
    import axios from 'axios'
    import 'bootstrap/dist/css/bootstrap.css'
    import 'jquery/dist/jquery.min.js'
    import 'bootstrap/dist/js/bootstrap.min.js'
    import { server } from "../../utils/helper.js";

    export default {
        data() {
            return {
                roleData: [],
                filteredResults:[],
                formattedDate: '',
                skills: [],
                allskills: [],
                selectedSkill: "",
            };
        },
        created() {
            this.getRole();
        },
        methods: {
            getRole() {
                const roleId = this.$route.params.roleId;
                console.log(roleId)

                // Make an Axios call with the roleId as a parameter
                axios.get(`http://localhost:5008/role/view_role`, {
                    params: {
                        role_id : roleId
                    }
                })
                .then(response => {
                    this.roleData = response.data; // Store the data
                    // Perform actions with the retrieved data
                    console.log(this.roleData);
                    const gmtDateString = this.roleData.App_Deadline;
                    const gmtDate = new Date(gmtDateString);
                    const year = gmtDate.getUTCFullYear();
                    const month = (gmtDate.getUTCMonth() + 1).toString().padStart(2, '0');
                    const day = gmtDate.getUTCDate().toString().padStart(2, '0');
                    const formattedDate = `${year}-${month}-${day}`;
                    this.formattedDate = formattedDate;

                    console.log(formattedDate); // you can use this formatted date to show in your app deadline
                })
                .catch(error => {
                    console.error('Error fetching role data:', error);
                });

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
            fetchroles() {
                axios.get("http://localhost:5008/roles/get_all_roles")
                .then(response => {
                    this.filteredResults = response.data.data.roles_with_details
                    console.log(this.filteredResults)
                })
                .catch(error => {
                    console.error("There was an error fetching the data:", error);
                });
            },
                 addSkillToSelectedSkills() {
                    if (this.selectedSkill) {
                        this.roleData.Role_Skills.push(this.selectedSkill);
                        this.selectedSkill = ""; // Reset the selected skill
                    }
                    },
                updateRoleSkills(skill) {
                const index = this.roleData.Role_Skills.indexOf(skill);
                if (index !== -1) {
                    this.roleData.Role_Skills.splice(index, 1);
                }
            },
            submitChanges() {
                // i want to ensure all fields are filled up before submitting if not alert user to fill up all fields
                if (this.roleData.Role_Name == '' || this.roleData.Role_Department == '' || this.roleData.Role_Description == '' || this.roleData.Role_Requirements == '' || this.roleData.Role_Skills == '' || this.formattedAppDeadline == '') {
                    alert("Please fill up all fields!");
                    return;
                }
                const dataToSend = {
                    Role_Name: this.roleData.Role_Name,
                    App_Deadline: this.formattedDate,
                    Role_Department: this.roleData.Role_Department,
                    Role_Description: this.roleData.Role_Description,
                    Role_Skills: this.roleData.Role_Skills,
                };
                axios
                    .put('http://localhost:5008/role/update?role_id=' + this.$route.params.roleId, dataToSend)
                    .then(response => {
                    if (response.status === 201) {
                        // Role updated successfully
                        alert(response.data.message);
                        // navigate to listing page
                    } else if (response.status === 200) {
                        // Role updated successfully
                        alert(response.data.message);
                        // i want to redirect the user back to hr-home after update is successful
                        this.$router.push({ name: 'HRHome' });

                    }
                    })
                    .catch(error => {
                    console.error('Error updating role:', error);
                    alert('Failed to update role. Please try again.');
                    });
                },
                addSkill() {
                    const skillName = event.target.innerText;
                    this.roleData.Role_Skills.push(skillName);
                    console.log(this.roleData.Role_Skills);
                },
                getSkills(){
                    axios.get('http://localhost:5008/skills/get_all_skills')
                    .then(response => {
                        this.skills = response.data.data.skills
                        console.log(this.skills)
                    })
                }

        },
    
            mounted() {
            // Use axios to fetch data from Flask API
            this.fetchroles();
            this.fetchskills();
            },
        };

    
</script>

<style>
/* Default styles for the button */
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

/* Responsive styles for smaller screens (e.g., screens with a max width of 768px) */
@media (max-width: 768px) {
  .top-left-button {
    font-size: 14px;
    padding: 8px 16px;
  }
}

/* Responsive styles for even smaller screens (e.g., screens with a max width of 480px) */
@media (max-width: 480px) {
  .top-left-button {
    font-size: 12px;
    padding: 6px 12px;
  }
}

</style>