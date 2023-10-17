<template>
    <div class="app">
        <div class="row m-3">
            <!-- back button to route back to the StaffHome page -->
            <div class="container-fluid back-btn col-3">
                <router-link to="/staff-home">
                    <button type="button" class="btn btn-secondary">Back</button>
                </router-link>
            </div>

            <!-- main body of role details -->
            <div class="container-fluid main col-6">
                <h2>{{ role.Role_Name }}</h2>
                <p style="color: grey;">Department: {{ role.Role_Department }} | Role ID: {{ role.Role_ID }}</p>
                <br>

                <p style="font-weight: bold;">Date Posted: <span style="font-weight: normal;">{{ getDeadlineYear(role.Date_Posted) }}</span></p>
                <p style="font-weight: bold;">Application Deadline: <span style="font-weight: normal;">{{ getDeadlineYear(role.App_Deadline) }}</span></p>
                <br>

                <h4> Job Description </h4>
                <p>{{ role.Role_Description }}</p>
                <br>
                
                <h4> Job Requirements </h4>
                <!-- <p> {{ role.Role_Requirements }}</p> -->
                <p v-html="role.Role_Requirements"></p>
                <!-- <p v-html="newline_to_br(role.Role_Requirements)"></p> -->

                <!-- have an apply now button in light blue, which will direct to a pop-up confirmation window to be linked later -->
                <button type="button" class="btn btn-info">Apply Now</button>
            </div>

            <!-- displaying the skills-matched percentage score -->
            <div class="container-fluid col-3">

            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { server } from "../../utils/helper.js"

    export default {
        name: 'roleListing',
        data() {
            return {
                role: {},
            };
        },
        computed: {
            roleId() {
                return this.$route.params.id
            }
        },
        created() {
            this.getRole()
        },
        methods: {
            getRole() {
                axios.get(`${server.baseURL}/role/view_role?role_id=${this.roleId}`)
                    .then(
                        (response) => {
                            this.role = response.data
                        }
                    ) 
                    .catch (
                        (error) => {
                            console.log(error)
                        }
                    )
            },
            getDeadlineYear(deadline) {
                const date = new Date(deadline)
                const year = date.getFullYear()
                return date.toDateString().replace(/\d{4}$/, year)
            },
            newline_to_br(text) {
                return text.replace(/\n/g, '<br>');
            },
        },
    };
</script>

<style>
    .back-btn {
        text-align: right
    }
    .main {
        text-align: left
    }
</style>