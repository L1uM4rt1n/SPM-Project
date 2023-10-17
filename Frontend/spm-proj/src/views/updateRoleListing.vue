<template>

    <div class="updateRoleListing container my-5">
    <div class="text-center">
        <h1 class="">Update Role Listing</h1>
    </div>
    
    <hr>
        <div class="container">
            <div class="form-group">
                <label for="exampleInputEmail1">Name</label>
                <input type="email" class="form-control" id="jobName" aria-describedby="jobName" placeholder="Enter Role Listing Name" style="margin-bottom: 15px;">
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
                        <option v-for="type in jobtypes" :key="type" :value="type">{{ type }}</option>
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
    import axios from 'axios'
    import { server } from "../../utils/helper.js"
    import 'bootstrap/dist/css/bootstrap.css'
    import 'jquery/dist/jquery.min.js'
    import 'bootstrap/dist/js/bootstrap.min.js'

    export default {
        name: 'StaffHome',
        data() {
            return {
                editing: false,
                editedRole: {
                    name: '',
                    description: '',

                },
            };
        },
        methods: {
            getAllRoles() {
                axios.get(`${server.baseURL}/role/view_role`)
                    .then(
                        (response) => {
                            this.roles = response.data.data.roles_with_details
                        }
                    )
            },
            editRole(){
                this.editing = true;
                // this.editedRole = {{this.previousRole}};
                axios.get(`${server.baseURL}/role/update/<int:role_id>`)
                    .then(
                        (response) => {
                            this.roles = response.data.data.roles_with_details
                        }
                )
            },
            saveRole(){
                this.editing = false;
            }
        },

    };
</script>
