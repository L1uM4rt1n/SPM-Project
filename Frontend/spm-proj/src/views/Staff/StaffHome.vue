<template>
    <div>
        <component :is="searchBarComponent" @search-request="performSearch" />
        <div class="container">
            <router-link to="'/role/' + role.slug" class="card-link" v-for="role in roles" :key="role.id">
                <div class="card rounded" style="border: 2px solid #ccc;">
                    <div class="card-body">
                        <h4 class="card-title">{{ role.role_name }}</h4>
                        <h6 class="card-text">Role ID: {{ role.role_id }}</h6>
                        <p class="card-text">Availability: {{ role.availability }}</p>
                        <p class="card-text">Application Deadline: {{ role.application_deadline }}</p>
                        <component :is="skillMatchPercentageComponent" :role-skills="role.skills" :staff-skills="staffSkills" />
                    </div>
                </div>
            </router-link>
        </div>
    </div>
</template>


<script>
    import axios from 'axios';
    import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
    import 'jquery/dist/jquery.min.js'; // Import jQuery
    import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

    export default {
        name: 'StaffPage',
        data() {
            return {
                roles: [],
                staffSkills: [],
                searchBarComponent: 'SearchBar',
                skillMatchPercentageComponent: null,
            };
        },
        created() {
            this.getRoles();
            this.getStaffSkills();
            this.loadSkillMatchPercentageComponent();
        },
        methods: {
            getRoles() {
                axios.get('/api/roles')
                    .then(response => {
                        this.roles = response.data.map(role =>  ({
                            role_name: role.role_name,
                            role_id: role.role_id,
                            availability: role.availability,
                            application_deadline: role.application_deadline,
                        }))
                    })
                    .catch(error => {
                        console.log(error);
                    });
            },
            getStaffSkills() {
                axios.get('/api/staff/skills')
                    .then(response => {
                        this.staffSkills = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            },
            loadSkillMatchPercentageComponent() {
                import('./SkillsMatchedPercentage.vue')
                    .then(module => {
                        this.skillMatchPercentageComponent = module.default;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            },
            performSearch(searchParams) {
                // perform search based on searchParams
                console.log(searchParams);
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