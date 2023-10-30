<template>
    <h2 style="margin: 10px;">{{roleName}}</h2>
    <p>Role ID: {{ $route.params.roleId }}</p>
    <router-link to="/hr-home">
      <button class="btn btn-light top-left-button">Back</button>
    </router-link>

    <div class="table-container m-5">
        <div class="table-scroll">
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

/* CSS to make the table scrollable */
.table-scroll {
  overflow-x: auto; /* Add horizontal scrollbar when content overflows */
  max-width: 100%; /* Ensure the table doesn't overflow its container */
}

/* Optional: Add a minimum width to the table so it doesn't collapse too much */
.table-scroll table {
  min-width: 600px; /* Adjust this value as needed */
}

</style>