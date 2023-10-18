<template>

    <div class="updateRoleListing container my-5">
    <div class="text-center">
        <h1 class="">Update Role Listing</h1>
        <p>Role ID: {{ $route.params.roleId }}</p>
    </div>
    
    <hr>
        <div class="container" style="text-align: left;">
            <div class="form-group">
                <label>Name</label>
                <input type="text" class="form-control" id="jobName" aria-describedby="jobName" style="margin-bottom: 15px;" v-model="roleData.Role_Name">
            </div>


            <div>
                Application Deadline <br>
                <input type="date" class="form-control" id="myDate" v-model="formattedAppDeadline"> 

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

            <div>
                <label for="exampleFormControlTextarea1" style="margin-top: 15px;">Role Requirements</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6" v-model="roleData.Role_Requirements"></textarea>
            </div>

            <!-- Checkboxes -->
            <div class="py-3">
                <label for="Skills">Skills Required</label><br>
                <div v-for="skill in roleData.Role_Skills" :key="skill" class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" :key="skill" :value="skill" checked>
                    <label class="form-check-label" for="inlineCheckbox1">{{skill}}</label>
                </div>
                    
                <!-- Additional 'Other' checkbox -->
                <input class="btn btn-secondary" type="button" value="+ Add Skills" @click="addSkill()">
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

    export default {
        data() {
            return {
                roleData: [],
                filteredResults:[],
                formattedAppDeadline: '' // Data retrieved from the server
            };
        },
        created() {
            this.getRole();
            // this.formattedAppDeadline = this.formatDate(this.roleData.App_Deadline);
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
                    console.log(this.roleData.Role_Name);
                })
                .catch(error => {
                    console.error('Error fetching role data:', error);
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
            editRole(){
                this.editing = true;
                // this.editedRole = {{this.previousRole}};
                axios.get(`http://localhost:5008/role/update/roleId`)
                    .then(
                        (response) => {
                            this.roles = response.data.data.roles_with_details
                        }
                )
            },
            saveRole(){
                this.editing = false;
            },
            submitChanges() {
                const dataToSend = {
                    Role_Name: this.roleData.Role_Name,
                    App_Deadline: this.formattedAppDeadline,
                    Role_Department: this.roleData.Role_Department,
                    Role_Description: this.roleData.Role_Description,
                    Role_Requirements: this.roleData.Role_Requirements,
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
                        // navigate to a listing page
                    }
                    })
                    .catch(error => {
                    console.error('Error updating role:', error);
                    alert('Failed to update role. Please try again.');
                    });
                },
        },
    
            mounted() {
            // Use axios to fetch data from Flask API
            this.fetchroles();
            },
        };

    
</script>
