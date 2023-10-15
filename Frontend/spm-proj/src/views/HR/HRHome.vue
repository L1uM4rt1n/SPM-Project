<template>
    <div class="app">

        <!-- display of all roles -->
        <div class="container">
            <!-- create role listing button -->
            <div class="d-flex flex-row justify-content-end" style="width:100%">
                <button class="btn btn-secondary border-dark my-2">Create Job Listing</button>
            </div>

            <div class="card rounded m-2" style="border: 2px solid #ccc;" v-for="role in roles" :key="role.Role_ID">
                <div class="card-body">
                    <h4 class="card-title">{{ role.Role_Name }}</h4>
                    <p class="card-text">Role ID: {{ role.Role_ID }}</p>
                    <p class="card-text">Role Availability: {{ role.Role_Availability }}</p>
                    <p class="card-text">Application Deadline: {{ getDeadlineYear(role.App_Deadline) }}</p>
                </div>
                <!-- edit button -->
                <div class="position-absolute bottom-0 end-0 m-2 edit-button">
                    <a :href="'#edit/' + role.id" class="btn btn-link" style="text-decoration: none;">Edit</a>
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
                            this.roles = response.data.data.bookings
                        }
                    )
            },
            getDeadlineYear(deadline) {
                const date = new Date(deadline)
                const year = date.getFullYear()
                return date.toDateString().replace(/\d{4}$/, year)
            }
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
