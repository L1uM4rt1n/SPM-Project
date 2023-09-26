<template>
      <div class="skill-match-percentage">
            <div class="skill-match-percentage-circle" :class="circleClass">
                  <div class="skill-match-percentage-text">{{ percentage }}%</div>
            </div>
      </div>
</template>

<script>
      import axios from 'axios';
      
      export default {
            name: 'SkillMatchPercentage',
            props: {
                  roleSlug: {
                        type: String,
                        required: true,
                  },
            },
            data() {
                  return {
                        roleSkills: [],
                        staffSkills: [],
                  };
            },
            computed: {
                  percentage() {
                        const matchedSkills = this.staffSkills.filter(skill => this.roleSkills.includes(skill));
                        return Math.round((matchedSkills.length / this.roleSkills.length) * 100);
                  },
                  circleClass() {
                        return {
                              'skill-match-percentage-circle-green': this.percentage >= 50,
                              'skill-match-percentage-circle-red': this.percentage < 50,
                        };
                  },
            },
            created() {
                  this.getStaffSkills();
                  this.getRoleSkills();
            },
            methods: {
                  getStaffSkills() {
                        axios.get('/api/staff/skills')
                              .then(response => {
                              this.staffSkills = response.data;
                              })
                              .catch(error => {
                              console.log(error);
                              });
                  },
                  getRoleSkills() {
                        axios.get(`/api/roles/${this.roleSlug}/skills`)
                              .then(response => {
                              this.roleSkills = response.data;
                              })
                              .catch(error => {
                              console.log(error);
                              });
                  },
            },
      };
</script>

<style>
      .skill-match-percentage {
            display: flex;
            justify-content: center;
            align-items: center;
      }
      
      .skill-match-percentage-circle {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background-color: #ccc;
            display: flex;
            justify-content: center;
            align-items: center;
      }
      
      .skill-match-percentage-text {
            font-size: 12px;
            font-weight: bold;
            color: #fff;
      }
      .skill-match-percentage-circle-green {
            background-color: #28a745;
      }
      
      .skill-match-percentage-circle-red {
            background-color: #dc3545;
      }
</style>
