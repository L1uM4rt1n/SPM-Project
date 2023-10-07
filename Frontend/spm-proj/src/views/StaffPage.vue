<template>
    <SearchBar
            v-model:keywordSearch="searchKeyword"
            :selectedSkills="selectedSkills"
            :selectedDepartments="selectedDepartments"
            @search-request="performSearch"
    />
    
    <div class="container">
        <router-link to="'/role/' + role.slug" class="card-link" v-for="role in roles" :key="role.id">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">{{ role.title }}</h4>
                    <h6 class="card-text">Role ID: {{  role.id }}</h6>
                    <p class="card-text">Availability: {{ role.availability }}</p>
                    <p class="card-text">Application Deadline: {{ role.deadline }}</p>
                </div>
            </div>
        </router-link>
    </div>

</template>

<script>
import SearchBar from '../components/SearchBar.vue';
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

    export default{
        name: 'StaffPage',
        components: {
            SearchBar,
        },
        data(){
            return{
                roles: [
                    {
                    id: 1,
                    title: 'Software Developer',
                    skills: ['Java', 'HTML'],
                    department: 'IT',
                    availability: 2,
                    deadline: '31/09/2002',
                    // slug: 'role-1'
                    },
                    {
                    id: 2,
                    title: 'Frontend Developer',
                    skills: ['HTML', 'CSS', 'JavaScript'],
                    department: 'HR',
                    availability: 2,
                    deadline: '26/09/2002',
                    // slug: 'role-2'
                    },
                ]
            }
        },
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

</style>

