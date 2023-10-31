<template>
    <div class="container mt-5">
        <div class="row d-flex justify-content-center">
            <div class="col-md-6">
                <div class="card px-5 py-5">
                    <h2 class="text-center mb-4">Login</h2>
                    <form @submit.prevent="authenticate">
                        <!-- access rights -->
                        <div class="form-group m-3">
                            <label for="access">Select Access</label>
                            <select id="access" v-model="access" class="form-control">
                                <option value="Staff">Staff</option>
                                <option value="HR">HR</option>
                            </select>
                        </div>
                        <!-- email field -->
                        <div class="form-group m-3">
                            <label for="email">Email</label>
                            <input
                                type="email"
                                id="email"
                                v-model="email"
                                class="form-control"
                                :class="{'is-invalid': emailBlurred && !validEmail(email)}"
                                @blur="emailBlurred = true"
                                required
                            />
                            <div class="invalid-feedback">A valid email is required!</div>
                        </div>
                        <!-- password field -->
                        <div class="form-group m-3">
                            <label for="password">Password</label>
                            <input
                                type="password"
                                id="password"
                                v-model="password"
                                class="form-control"
                                :class="{'is-invalid': passwordBlurred && !validPassword(password)}"
                                @blur="passwordBlurred = true"
                                required
                            />
                            <div class="invalid-feedback">A valid password is required!</div>
                        </div>
                        <!-- login button -->
                        <button @click="authenticate" class="btn btn-dark w-auto m-3">Login</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { server } from "../utils/helper.js"

    export default {
        name: 'LoginPage',
        data() {
            return {
                access: 'Staff',
                accessRights: '',
                staffID: '',
                password: '',
                email: '',
                submitted: false,
                emailBlurred: false,
                passwordBlurred: false,
                // flag to prevent 2x output of data in console to reduce load
                isAuthenticating: false,
            }
        },
        methods: {
            authenticate() {
                if (this.isAuthenticating) {
                    return
                }

                this.isAuthenticating = true
                // Check if access is 'Staff' or 'HR'
                if (this.access === 'Staff' || this.access === 'HR') {
                    this.accessRights = this.access
                    axios.post(`${server.baseURL}/login`, {
                        Email: this.email,
                        Password: this.password,
                        Access_Role: this.access,
                    })
                    .then((response) => {
                        if (response.status === 200) {
                            const data = response.data.data
                            if (data.Access_Role === 4) {
                                sessionStorage.setItem('user', JSON.stringify(data))
                                this.$router.push({ name: 'HRHome' })
                            } else if (data.Access_Role === 2) {
                                sessionStorage.setItem('user', JSON.stringify(data));
                                this.$router.push({ name: 'StaffHome' })
                            }
                        } else if (response.status === 404) {
                            alert('Please enter valid credentials')
                        } else if (response.status === 401) {
                            if (response.data.message === "Incorrect password") {
                                alert("Please enter a valid password")
                            } else if (response.data.message === "Restricted Access") {
                                alert("Please select the correct access")
                            }
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                } else {
                    // Handle invalid "access" value (e.g., show an error message)
                    alert('Invalid access');
                }
            },
            validEmail(email) {
                return axios.post(`${server.baseURL}/validate-email`, { email })
                    .then((response) => {
                        return response.data.valid;
                })
                    .catch((error) => {
                        console.log(error);
                        return false;
                });
            },
            validPassword(password) {
                return axios.post(`${server.baseURL}/validate-password`, { password })
                    .then((response) => {
                        return response.data.valid;
                    })
                    .catch((error) => {
                        console.log(error);
                        return false;
                    });
            },
        }
    }
</script>

<style>
</style>