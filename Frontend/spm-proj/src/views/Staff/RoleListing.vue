<template>
    <div class="container">
        <h1>Role Listing Page</h1>
        <h2>{{ role.Role_Name }}</h2>
        <p>{{ role.Role_Description }}</p>
        <p>Deadline: {{ role.deadline }}</p>
    </div>
</template>

<script>
    import axios from 'axios';
    import { server } from "../../utils/helper.js"

    export default {
        name: 'roleListing',
        props: {
            id: {
                type: Number,
                required: true
            }
        },
        data() {
            return {
                role: {},
            };
        },
        methods: {
            getRole() {
                axios.get(`${server.baseURL}/role/view_role?role_id=${this.id}`)
                    .then(
                        (response) => {
                            this.roles = response.data
                            console.log(this.roles)
                        }
                    )
            },
        },
    };
</script>

<style>

</style>