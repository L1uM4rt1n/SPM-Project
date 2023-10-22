<!-- Template -->
<template>
    <div class="container mt-5">
    <div class="row d-flex justify-content-center">
        <div class="col-md-6">
        <div class="card px-5 py-5" id="form1">
            <div class="form-data">
                <div class="forms-inputs mb-4">
                    <label for="access">Select Access</label>
                    <select
                        id="access"
                        v-model="access"
                        class="form-select"
                    >
                        <option value="Staff">Staff</option>
                        <option value="HR">HR</option>
                    </select>
                </div>
            <div class="forms-inputs mb-4">
                <label for="email">Email</label>
                <input autocomplete="off"
                type="text"
                id="email"
                v-model="email"
                :class="{'form-control': true, 'is-invalid': emailBlurred && !validEmail(email)}"
                @blur="emailBlurred = true"
                />
                <div class="invalid-feedback">A valid email is required!</div>
            </div>
            <div class="forms-inputs mb-4">
                <label for="password">Password</label>
                <input
                autocomplete="off"
                type="password"
                id="password"
                v-model="password"
                :class="{'form-control': true, 'is-invalid': passwordBlurred && !validPassword(password)}"
                @blur="passwordBlurred = true"
                />
                <div class="invalid-feedback">Password must be at least 3 characters long!</div>
            </div>
            <div class="mb-3">
                <button @click="authenticate" class="btn btn-dark w-100">Login</button>
            </div>
            </div>
            <div class="success-data" v-if="submitted">
            <div class="text-center d-flex flex-column">
                <i class="bx bxs-badge-check"></i>
                <span class="text-center fs-1">You have been logged in <br> Successfully</span>
            </div>
            </div>
        </div>
        </div>
    </div>
    </div>
</template>


<!-- Script -->
<script>
import 'bootstrap/dist/css/bootstrap.css';
import 'jquery/dist/jquery.min.js';
import 'bootstrap/dist/js/bootstrap.min.js';
import axios from 'axios';

export default {
    name: 'LoginPage',
    components: {},
    data() {
    return {
        access: 'Staff',
        accessRights: '',
        staffID: '',
        password: '',
        email: '', // Add an email data property
        submitted: false,
        emailBlurred: false,  // Corrected the spelling here
        passwordBlurred: false,  // Corrected the spelling here
    };
    },
    created() {
    },
    methods: {
        authenticate() {
            // Check if access is 'Staff'
            if (this.access === 'Staff') {
                this.accessRights = 'staff';
                axios.post('http://localhost:5008/login', {
                    Email: this.email,
                    Password: this.password,
                    Access_Rights: this.access,
                })
                .then((response) => {
                    console.log(response);
                    if (response.status === 200) {
                        console.log(response.data);
                        sessionStorage.setItem('user', JSON.stringify(response.data));
                        this.$router.push({ name: 'StaffHome' }); // Redirect to Staff page
                    } else {
                    alert('Invalid Credentials');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
            }
            // Check if access is 'HR'
            else if (this.access === 'HR') {
                this.accessRights = 'hr';
                axios.post('http://localhost:5008/login', {
                    Email: this.email,
                    Password: this.password,
                    Access_Rights: this.access,
                })
                .then((response) => {
                    console.log(response);
                    if (response.status === 200) {
                        sessionStorage.setItem('Access', this.access);
                        sessionStorage.setItem('Email', this.email);
                        this.$router.push({ name: 'HRHome' }); // Redirect to HR page
                    } else {
                    alert('Invalid Credentials');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
            } else {
                // Handle invalid "access" value (e.g., show an error message)
                alert('Invalid access');
            }
            },

    validEmail(email) {
      // Implement your email validation logic here
      // For example, you can use a regular expression
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    },
    validPassword(password) {
      // Implement your password validation logic here
      // For example, check if the password has a minimum length
        return password.length >= 3;
    },
    },
};

</script>

<!-- Styling -->
<style>
</style>