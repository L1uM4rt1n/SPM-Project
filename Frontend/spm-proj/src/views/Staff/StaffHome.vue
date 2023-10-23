<template>
    <div class="app">
        <!-- Search Bar -->
        <SearchBar
            v-model="searchKeyword"
            :selectedSkills="selectedSkills"
            :selectedDepartments="selectedDepartments"
            @search-request="performSearch"
        />
        <!-- display of all roles -->
        <div class="container">
            <div class="card rounded m-2" style="border: 2px solid #ccc;" v-for="role in filteredResults" :key="role.Role_ID">
                <div class="card-body">
                    <h4 class="card-title black-bold">{{ role.Role_Name }}</h4>
                    <p class="card-text black-bold">Role ID: {{ role.Role_ID }}</p>
                    <p class="card-text black-bold">Role Availability: {{ role.Availability }}</p>
                    <p class="card-text black-bold">Application Deadline: {{ getDeadlineYear(role.App_Deadline) }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import SearchBar from '../../components/SearchBar.vue'
    import axios from 'axios'
    import { server } from "../../utils/helper.js"

    export default{
        name: 'StaffHome',
        components: {
            SearchBar,
        },
        data() {
            return {
                selectedSkills: [],
                selectedDepartments: [],
                searchKeyword: '',
                roles: [],
                filteredResults:[],
                user: null,
            };
        },
        methods: {
            performSearch(payload) {
                if (payload) {
                    const { keyword, selectedDepartments, selectedSkills } = payload;

                    // Filter the role listings based on selected departments, skills, and keyword
                    const filteredResults = this.roles.filter((role) => {
                        const hasSelectedDepartment =
                            selectedDepartments.length === 0 ||
                            selectedDepartments.includes(role.Role_Department)

                        const hasSelectedSkills =
                            selectedSkills.length === 0 ||
                            selectedSkills.some((selectedSkill) =>
                                role.Role_Skills.includes(selectedSkill)
                            )

                        // Check for a keyword match in both the role name and description
                        const keywordMatch =
                        (role.Role_Name &&
                            role.Role_Name.toLowerCase().includes(keyword.toLowerCase())) ||
                        (role.Role_Description &&
                            role.Role_Description.toLowerCase().includes(keyword.toLowerCase()))

                        return hasSelectedDepartment && hasSelectedSkills && keywordMatch
            });
                    this.filteredResults = filteredResults;
                }
            },
            getAllRoles() {
                axios.get(`${server.baseURL}/roles/get_all_roles`)
                    .then(
                        (response) => {
                            this.roles = response.data.data.roles_with_details

                            const today = new Date()
                            this.filteredResults = this.roles.filter(role => {
                                const deadline = new Date(role.App_Deadline)
                                return deadline >= today
                            })
                        }
                    )
            },
            getDeadlineYear(deadline) {
                const date = new Date(deadline)
                const year = date.getFullYear()
                return date.toDateString().replace(/\d{4}$/, year)
            },
        },

        watch: {
            // Watch for changes to the searchKeyword and trigger performSearch
            searchKeyword: function() {
                this.performSearch(); // Call the performSearch method when searchKeyword changes
            },
        },

        created() {
            this.getAllRoles();
            this.user = JSON.parse(sessionStorage.getItem('user'))

        }
    }
</script>

<style>
    .circle{
        width: 10px;
        height: auto;
        border-radius: 50%;
        text-align: center;
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

