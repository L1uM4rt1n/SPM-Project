<template>
    <h2 style="margin: 10px;">{{roleName}}</h2>
    <p>Role ID: {{ $route.params.roleId }}</p>
    <router-link to="/hr-home">
      <button class="btn btn-light top-left-button">Back</button>
    </router-link>

    <div class="table-container m-5">
        <table class="table table-hover">
        <thead>
            <tr>
                <th scope="col">Application ID</th>
                <th scope="col">Applicant Name</th>
                <th scope="col">Applicant Email</th>
                <th scope="col">Applicant Department</th>
                <th scope="col">Applicant Country</th>
                <th scope="col">Applicant Skills</th>
                <th scope="col">Percentage Skill Match</th>
                
            </tr>
        </thead>
        <tbody>
            <tr v-for="app in application" :key="app.Application_ID">
                <th scope="row">{{ app.Applicant_ID }}</th>
                <td>{{ app.Applicant_Name}}</td>
                <td>{{ app.Applicant_Email }}</td>
                <td>{{ app.Applicant_Department }}</td>
                <td>{{ app.Applicant_Country }}</td>
                <td>
                    <ul style="list-style-type: none; margin: 0; padding: 0;">
                    <li v-for="skill in app.Applicant_Skills" :key="skill">{{ skill }}</li>
                    </ul>
                </td>
                <td>{{ app.Applicant_Skills_Percentage_Matched }}</td>
            </tr>
        </tbody>
    </table>

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
                application: [],
                roleName : '',
                roleData: [],
            };
        },
        created() {
            const roleId = this.$route.params.roleId;
            this.getRole(roleId); // Pass it to the function that sets roleName
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
                    this.roleName = this.roleData.Role_Name;
                    this.getApplication(this.roleName);
                    console.log(this.roleName)

                })
                .catch(error => {
                    console.error('Error fetching role data:', error);
                });

            },
            // getApplication(roleName){
            //     if (!roleName) {
            //         console.error('Role name is not set.');
            //         return;
            //     }
            //     axios.get(`http://localhost:5008/role/${roleName}/applicants/skills`, {
            //         params: {
            //             role_name: roleName
            //         }
            //     })
            //     .then(response => {
            //         console.log(roleName)
            //         this.application = response.data; // Store the data
            //         console.log(this.application);
            //     })
            //     .catch(error => {
            //         console.error('Error fetching role data:', error);
            //     });
            
            getApplication(roleName) {
            axios.get('http://localhost:5008/role_application/applicants/skills', {
                params: {
                    
                    role_name: roleName
                }
            })
            .then(response => {
                // Check if the response code is 200 (Success)
                if (response.data.code === 200) {
                    this.application = response.data.data;
                    console.log('Applicant Skills Data:', this.application);
                } else {
                    console.error('Error:', response.data.message);
                    // Handle other response codes if needed
                }
            })
            .catch(error => {
                console.error('Error fetching applicant skills data:', error);
            });
                
            }
            
        },
        mounted() {
            this.getApplication();
        },
    };

</script>

<style>
  .top-left-button {
    position: absolute;
    top: 120px;
    left: 50px;
    margin: 10px; /* Add margin for spacing */
  }
</style>