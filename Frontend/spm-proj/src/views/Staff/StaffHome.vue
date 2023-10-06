<template>
    <div class="app">
        <!-- dynamic search bar -->

        <!-- display of all roles -->
        <div class="container">
            <div class="card rounded" style="border: 2px solid #ccc;" v-for="role in roles" :key="role.Role_ID">
                <div class="card-body">
                    <h4 class="card-title">{{ role.Role_Name }}</h4>
                    <p class="card-text">Role ID: {{ role.Role_ID }}</p>
                    <p class="card-text">Application Deadline: {{ role.App_Deadline }}</p>
                </div>
            </div>
        </div>

        <!-- tester -->
        <ul>
            <li v-for="role in roles" :key="role.role_id">
                {{ role.role_name }}
            </li>
        </ul>
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
                roles: [],
            };
        },
        created() {
            this.getAllRoles();
        },
        methods: {
            getAllRoles() {
                axios.get(`${server.baseURL}/roles/get_all_roles`)
                    .then(
                        (response) => {
                            // console.log(response)
                            this.roles = response.data.data.bookings
                        }
                    )
                    // .catch((error) => {
                    //     console.error(error)
                    // });
            },
        },
    };
</script>

<style>
    .circle {
        width: 10px;
        height: auto;
        border-radius: 50%;
        text-align: center;
        border: 1px solid #ccc;
    }
    .card-link{
        text-decoration: none;
    }
</style>