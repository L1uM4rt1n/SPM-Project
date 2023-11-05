<template>
      <div class="profile container my-5">
    <div class="text-center">
        <h1 class="">Your Profile</h1>
        <h6> Staff ID: {{staff_id}} </h6>
    </div>
    
    <hr>
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                <h4> My Details </h4>
                    <div class="card mb-3">
                        <div class="card-body">
                            <div class="row">
                                <div class="col-sm-3">
                                    <h6 class="mb-0">Full Name</h6>
                                </div>
                                <div class="col-sm-9 text-secondary">
                                    {{ staff_fname }} {{ staff_lastname }}
                                </div>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <h6 class="mb-0">Email</h6>
                            </div>
                            <div class="col-sm-9 text-secondary">
                                {{ email }}
                            </div>
                        </div>
                            <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <h6 class="mb-0">Department</h6>
                            </div>
                            <div class="col-sm-9 text-secondary">
                                {{ dept }}
                            </div>
                        </div>
                            <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <h6 class="mb-0">Country</h6>
                            </div>
                            <div class="col-sm-9 text-secondary">
                                {{ country }}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <h4 class="material-icons mr-2">My Skills</h4>
                    <div class="card mb-3">
                        <div class="card-body text-center">
                        <div v-for="skill in staff_skills" :key="skill" class="mx-auto">{{ skill }}<hr></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <h4> My Applications </h4>
            <div class="card">
                <div class="table-scroll">
                    <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Role ID</th>
                            <th scope="col">Role Name</th>
                            <th scope="col">Role Department</th>  
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="app in filteredapplied" :key="app.Application_ID">
                            <th scope="row">{{ app.Role_ID }}</th>
                            <td>{{ app.Role_Name}}</td>
                            <td>{{ app.Role_Department }}</td>
                        </tr>
                    </tbody>
                </table>
                <h5 v-if="filteredapplied.length ==0" style="text-align: center;"> {{noApp}} </h5>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS
import axios from 'axios';
import { server } from "../utils/helper.js";

export default {
  name: 'profile-page', 
  data() {
    return {
        userData: JSON.parse(sessionStorage.getItem('user')),
        country: JSON.parse(sessionStorage.getItem('user')).Country,
        dept: JSON.parse(sessionStorage.getItem('user')).Dept,
        email: JSON.parse(sessionStorage.getItem('user')).Email,
        staff_fname: JSON.parse(sessionStorage.getItem('user')).Staff_FName,
        staff_id: JSON.parse(sessionStorage.getItem('user')).Staff_ID,
        staff_lastname: JSON.parse(sessionStorage.getItem('user')).Staff_LName,
        filteredResults: '',
        staff_skills: [],
        filteredapplied: '',
        noApp: '',
        

    };
  },
  methods: {
    test() {
        console.log(this.userData)
        console.log(this.country)
        console.log(this.dept)
        console.log(this.email)
        console.log(this.staff_fname)
        console.log(this.staff_id)
        console.log(this.staff_lastname)
    },
    fetchroles(staff_id) {
        axios.get(`${server.baseURL}/staff/get_profile`, {
        params: { staff_id: staff_id }
        })
        .then(response => {
        this.filteredResults = response.data.staff_profile;
        this.staff_skills = response.data.staff_profile.Staff_Skills;
        console.log(this.filteredResults);
        console.log(this.staff_skills)
        })
        .catch(error => {
        console.error("There was an error fetching the data:", error);
        });
    },
    fetchapplied(staff_id) {
        axios.get(`${server.baseURL}/staff/applied_roles`, {
        params: { staff_id: staff_id }
        })
        .then(response => {
            this.filteredapplied = response.data.data;
            console.log(this.filteredapplied);
        })
        .catch(error => {
        console.error("There was an error fetching the data:", error);
        this.noApp = error.response.data.message
        });
    },
    },
  mounted() {
        // Use axios to fetch data from Flask API
        this.fetchroles(this.staff_id);
        this.fetchapplied(this.staff_id);
    },
};



</script>
