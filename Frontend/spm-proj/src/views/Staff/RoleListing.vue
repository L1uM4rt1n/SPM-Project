<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <nav class="navbar navbar-light bg-light">
                    <!-- Back Button -->
                    <router-link :to="{ name: 'StaffHomePage' }">
                        <a class="navbar-brand">
                        <i class="fas fa-chevron-left"></i> Back
                        </a>
                    </router-link>
                </nav>
            </div>
        </div>

        <div class="row mt-3">
            <div class="col-12">
                <div class="card">
                    <!-- Role Details -->
                    <div class="card-body d-flex justify-content-between align-items-center">
                        <h5 class="card-title text-left">{{ role.name }} ({{ role.department }})</h5>
                        <div class="d-flex align-items-center ml-auto">
                            <skill-matched-percentage :role-slug="role.slug" />
                        </div>
                        
                        <p class="card-text text-left">
                            <strong>Date Posted:</strong> {{ role.datePosted }}<br>
                            <strong>Application Deadline:</strong> {{ role.applicationDeadline }}<br>
                        </p>
                        
                        <hr>
                        
                        <p class="card-text text-left">
                            <strong>Job Expectations:</strong> {{ role.jobExpectations }}<br>
                            <strong>Job Description:</strong> {{ role.jobDescription }}<br>
                        </p>
                        <p class="card-text text-left">
                            <span v-for="(skill, index) in role.skills" :key="index" :class="{ 'text-success': isSkillMatched(skill), 'text-danger': !isSkillMatched(skill) }">
                                {{ skill }}<span v-if="index < role.skills.length - 1">, </span>
                            </span>
                        </p>
                        
                        <button class="btn btn-primary">Apply Now</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import SkillMatchedPercentage from '../../components/SkillsMatchedPercentage.vue';
    import axios from 'axios';

    export default {
        name: 'RoleListing',
        components: {
            SkillMatchedPercentage,
        },
        props: {
            roleSlug: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                role: {},
                staffSkills: [],
            };
        },
        created() {
            this.getRole();
            this.getStaffSkills();
        },
        methods: {
            getRole() {
                axios.get(`/api/roles/${this.roleSlug}`)
                    .then(response => {
                        this.role = response.data;
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
            isSkillMatched(skill) {
                return this.staffSkills.includes(skill);
            },
        },
    };
</script>

<style>
    .skill-matched {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 1.2rem;
    color: #fff;
    }
    .back-button:hover,
    .apply-now-button:hover,
    .skill-match-percentage:hover {
    transform: scale(1.1);
    border: 1px solid black;
    }

    .role-name {
    font-size: 24px;
    font-weight: bold;
    }

    .card-text {
    font-size: 14px;
    }
</style>