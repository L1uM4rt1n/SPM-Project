<template>
    <div class="app">

        <!-- display of all roles -->
        <div class="container">
            <div class="card rounded m-2" style="border: 2px solid #ccc;" v-for="role in filteredRoles" :key="role.Role_ID">
                <div class="card-body">
                    <h4 class="card-title black-bold">{{ role.Role_Name }}</h4>
                    <p class="card-text black-bold">Role ID: {{ role.Role_ID }}</p>
                    <p class="card-text black-bold">Role Availability: {{ role.Role_Availability }}</p>
                    <p class="card-text black-bold">Application Deadline: {{ getDeadlineYear(role.App_Deadline) }}</p>
                </div>
            </div>
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
                            this.roles = response.data.data.roles_with_details
                        }
                    )
            },
            getDeadlineYear(deadline) {
                const date = new Date(deadline)
                const year = date.getFullYear()
                return date.toDateString().replace(/\d{4}$/, year)
            }
        },
        computed: {
            filteredRoles() {
                const today = new Date()
                return this.roles.filter(role => {
                    const deadline = new Date(role.App_Deadline)
                    return deadline >= today
                })
            }
        }
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
    .black-bold {
        color: black;
    }
    .black-bold:hover {
        color: black;
        font-weight: bold;
    }
</style>
