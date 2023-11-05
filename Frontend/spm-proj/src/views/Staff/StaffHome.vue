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
                <router-link :to="{ name: 'roleListing', params: { id: role.Role_ID } }">
                    <div class="card-body">
                        <h4 class="card-title black-bold">{{ role.Role_Name }}</h4>
                        <p class="card-text black-bold">Role ID: {{ role.Role_ID }}</p>
                        <p class="card-text black-bold">Application Deadline: {{ getDeadlineYear(role.App_Deadline) }}</p>
                    </div>
                    <div class="skills-matched position-absolute top-0">
                        <div v-if="getRelevantPercentageMatch(role.Role_Name) > 0" class="circle" :class="{ 'green': getRelevantPercentageMatch(role.Role_Name) >= 50, 'red': getRelevantPercentageMatch(role.Role_Name) < 50}">
                            {{  getRelevantPercentageMatch(role.Role_Name) }}%
                        </div>
                        <div v-else class="circle red">
                            0%
                        </div>
                    </div>
                </router-link>
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
                filteredResults: [],
                user_id: JSON.parse(sessionStorage.getItem('user')).Staff_ID,
                skillsMatched: [],
                appliedRoles: [],
            };
        },

        created() {
            this.getAllRoles()
            this.getPercentageMatch()
            this.getAppliedRoles()
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
            getAppliedRoles() {
                axios.get(`${server.baseURL}/staff/applied_roles?staff_id=${this.user_id}`)
                    .then(
                        (response) => {
                            this.appliedRoles = response.data.data
                        }
                    )
            },
            getAllRoles() {
                axios.get(`${server.baseURL}/roles/get_all_roles`)
                    .then(
                        (response) => {
                            this.roles = response.data.data.roles_with_details

                            const today = new Date()
                            this.filteredResults = this.roles.filter(role => {
                                const deadline = new Date(role.App_Deadline)
                                const notApplied = !this.appliedRoles.some(appliedRole => appliedRole.Role_ID === role.Role_ID)
                                return deadline >= today && notApplied
                            })
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
                            this.skillsMatched = response.data.data
                        }
                    )
            },
            getRelevantPercentageMatch(roleName) {
                const role = this.skillsMatched.find(role => role.Role_Name === roleName)
                return role ? parseFloat(role.Percentage_Matched) : 0;
            },
        },

        watch: {
            // Watch for changes to the searchKeyword and trigger performSearch
            searchKeyword: function() {
                this.performSearch(); // Call the performSearch method when searchKeyword changes
            },
        },
    }
</script>

<style>
    .circle{
        width: 70px;
        height: 70px;
        border-radius: 50%;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
    }

    .red {
        background-color: rgb(255, 89, 89);
    }

    .green {
        background-color: rgb(61, 176, 61);
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

    .skills-matched {
        position: absolute;
        right: 0;
        margin: 30px;
    }
</style>
