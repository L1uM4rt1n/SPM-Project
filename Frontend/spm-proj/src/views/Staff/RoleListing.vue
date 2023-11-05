<template>
    <div class="app" v-if="role && percentageMatch != null">
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

                <!-- displaying the skillsMatched in green and skillsGap in red, all under 1 single Skills Required header -->
                <h4> Skills Matched </h4>
                <p v-for="(skill, index) in skillsMatched" :key="'matched-' + index" style="color: rgb(61, 176, 61);"> {{ skill }} </p>
                <p v-for="(skill, index) in skillsGap" :key="'gap-' + index" style="color: rgb(255, 0, 0);"> {{ skill }} </p>

                <!-- have an apply now button in light blue, which will direct to a pop-up confirmation window to be linked later -->
                <button @click="applyNow" type="button" class="btn btn-info">Apply Now</button>
            </div>

            <!-- displaying the skills-matched percentage score -->
            <div class="container-fluid skills-matched col-3"> 
                <div class="circle" :class="{ 'green': parseFloat(percentageMatch.replace('%', '')) >= 50, 'red': parseFloat(percentageMatch.replace('%', '')) < 50 }">
                    {{ percentageMatch }}
                </div>
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
                role: null,
                user_id: JSON.parse(sessionStorage.getItem('user')).Staff_ID,
                percentageMatch: null,
                skillsMatched: [],
                skillsGap: [],
            };
        },
        computed: {
            roleId() {
                return this.$route.params.id
            },
        },
        created() {
            this.getRole(),
            this.getPercentageMatch()
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
            getPercentageMatch() {
                axios.get(`${server.baseURL}/staff/role-matches?staff_id=${this.user_id}`)
                    .then(
                        (response) => {
                            // console.log(response.data.data)
                            for (let tempRole of response.data.data) {
                                if (tempRole.Role_Name === this.role.Role_Name) {
                                    this.percentageMatch = tempRole.Percentage_Matched
                                    this.skillsMatched = tempRole.Skills_Matched
                                    this.skillsGap = tempRole.Skills_Gap
                                }
                            }
                        }
                    )
                    .catch(
                        (error) => {
                            console.error(error)
                        }
                    )
            },
            applyNow() {
                axios.post(`${server.baseURL}/staff/submit_application?role_id=${this.role.Role_ID}&staff_id=${this.user_id}`)
                    .then(
                        (response) => {
                            console.log(response.data)
                            alert("Application submitted successfully.")
                        }
                    )
                    .catch(
                        (error) => {
                            console.error(error)
                            alert("You have already applied for this role.")
                        }
                    )
            }
        },
    };
</script>

<style>
    .back-btn {
        text-align: center
    }
    .main {
        text-align: left
    }
    .circle{
        width: 70px;
        height: 70px;
        border-radius: 50%;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        z-index: 1000;
    }
    .red {
        background-color: rgb(255, 89, 89);
    }
    .green {
        background-color: rgb(61, 176, 61);
    }
    .skills-matched {
        text-align: center;
        z-index: 1000;
    }
</style>