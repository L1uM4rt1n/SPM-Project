<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <!-- Your Bootstrap search bar HTML here -->
                <div class="input-group my-5" id="adv-search">

                    <input
                        type="text"
                        class="form-control border-secondary"
                        placeholder="Search for job listings"
                        v-model="searchKeyword"
                        @keyup.enter = "triggerSearch"
                        style ="border-right: 0; border-color: transparent;"
                    />

                    <div class="input-group-append">
                        <button class="btn border-secondary" @click="clearSearch" style ="border-left: 0; border-color: transparent; border-radius:0">X
                        </button>
                    </div>

                    <!-- <button type="button" class="btn btn-outline-secondary btn-close" aria-label="Close" @click="clearSearch" ></button> -->
                    <div class="dropdown" @click.stop>
                        <button
                            type="button"
                            class="btn btn-outline-secondary"
                            @click="toggleDropdown"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                class="bi bi-filter"
                                viewBox="0 0 16 16"
                            >
                                <path
                                    d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"
                                />
                            </svg>
                        </button>

                        <ul ref="secondaryMenu" class="dropdown-menu dropdown-menu-end secondary-dropdown-menu" :class="{ show: isDropdownOpen }">
                            <li>
                                <h5 class="">Select Departments:</h5>
                            </li>
                            <li>
                                <div class="dropdown">
                                    <button
                                        class="btn btn-secondary dropdown-toggle"
                                        type="button"
                                        @click="toggleDepartmentsDropdown"
                                    >
                                        {{ selectedDepartments.length === 0 ? 'Select departments' : selectedDepartments.join(', ') }}
                                    </button>
                                    <ul class="dropdown-menu" :class="{ show: isDepartmentsDropdownOpen }">
                                        <li v-for="department in departments" :key="department.id" class="my-1 mx-3">
                                        <input
                                            type="checkbox"
                                            class="form-check-input"
                                            :id="'department_' + department.id"
                                            :value="department.name"
                                            v-model="selectedDepartments"
                                            style="max-width: 150px;"
                                        />
                                            <label class="form-check-label" :for="'department_' + department.id">{{ department.name }}</label>
                                        </li>
                                    </ul>
                                </div>
                            </li>
                            <li>
                                <h5 class="mt-3">Select Skills:</h5>
                            </li>
                            <li>
                                <div class="dropdown">
                                    <button
                                        class="btn btn-secondary dropdown-toggle"
                                        type="button"
                                        @click="toggleSkillsDropdown"
                                    >
                                        {{ selectedSkills.length === 0 ? 'Select skills' : selectedSkills.join(', ') }}
                                    </button>
                                    <ul class="dropdown-menu" :class="{ show: isSkillsDropdownOpen }">
                                        <li v-for="skill in skills" :key="skill.id" class="my-1 mx-3">
                                            <input
                                                type="checkbox"
                                                class="form-check-input"
                                                :id="'skill_' + skill.id"
                                                :value="skill.name"
                                                v-model="selectedSkills"
                                                style="max-width: 150px;"
                                            />
                                            <label class="form-check-label" :for="'skill_' + skill.id">{{ skill.name }}</label>
                                        </li>
                                    </ul>
                                </div>
                            </li>
                            <li>
                                <a class="btn btn-link mt-3" @click="clearSelection">Clear Selection</a>
                            </li>
                        </ul>
                    </div>
                    <button type="button" class="btn btn-outline-secondary" @click="triggerSearch" id="searchButton">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="16"
                            height="16"
                            fill="currentColor"
                            class="bi bi-search"
                            viewBox="0 0 16 16"
                        >
                            <path
                                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
                            />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
    import "bootstrap/dist/css/bootstrap.min.css"
    import "bootstrap"  
    //   import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 5 CSS
    //   import 'jquery/dist/jquery.min.js'; // Import jQuery
    //   import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 5 JS
    
    export default {
      name: 'SearchBar',
      data() {
      return {
          isDropdownOpen: false,
          isSkillsDropdownOpen: false,
          isDepartmentsDropdownOpen: false,
          skills: [
          { id: 1, name: 'JavaScript' },
          { id: 2, name: 'HTML' },
          { id: 3, name: 'CSS' },
          { id: 4, name: 'Analytics' },
          { id: 5, name: 'Excel' },
          { id: 6, name: 'UX/UI' },
          // Add more skills as needed
          ],
          selectedSkills: [],
          departments: [
          { id: 1, name: 'HR' },
          { id: 2, name: 'Marketing' },
          { id: 3, name: 'Finance' },
          { id: 4, name: 'IT' },
          // Add more departments as needed
          ],
          selectedDepartments: [],
          searchKeyword: '',
      };
      },
      methods: {
          toggleDropdown() {
              this.isDropdownOpen = !this.isDropdownOpen;
          },
          toggleSkillsDropdown() {
              this.isSkillsDropdownOpen = !this.isSkillsDropdownOpen;
          },
          toggleDepartmentsDropdown() {
              this.isDepartmentsDropdownOpen = !this.isDepartmentsDropdownOpen;
          },
          clearSelection() {
              this.selectedSkills = [];
              this.selectedDepartments = [];
          },
          clearSearch(){
              this.searchKeyword = ''
              this.triggerSearch()
          },
          triggerSearch() {
              this.$emit('search-request', {
              keyword: this.searchKeyword,
              selectedDepartments: this.selectedDepartments,
              selectedSkills: this.selectedSkills,
              });
          },
          handleClickOutside(event) {
              // Check if the click target is inside the secondary menu
              const secondaryMenu = this.$refs.secondaryMenu; // Add ref to your secondary menu
              if (secondaryMenu && !secondaryMenu.contains(event.target)) {
                  // Click occurred outside the secondary menu, close it
                  this.isDropdownOpen = false;
              }
          },
          beforeDestroy() {
              // Remove the event listener when the component is destroyed
              document.removeEventListener('click', this.handleClickOutside);
          },
  
      },
      mounted() {
      const searchButton = document.getElementById('searchButton');
      searchButton.addEventListener('click', this.triggerSearch);
  
      searchButton.addEventListener("keypress", (event) => {
          if (event.key === "Enter") {
          this.triggerSearch();
          }
      })
      // Add an event listener to the document for clicks
      document.addEventListener('click', this.handleClickOutside);
      },
  
  };
</script>

<style>
    /* Add component-specific styles here */
    .form-check-input {
        margin-right: 15px; /* Adjust the margin value as needed */
    }

    .dropdown.dropdown-lg .dropdown-menu {
        margin-top: -1px;
        padding: 6px 20px;
    }
    .input-group-btn .btn-group {
        display: flex !important;
    }
    .btn-group .btn {
        border-radius: 0;
        margin-left: -1px;
    }
    .btn-group .btn:last-child {
        border-top-right-radius: 4px;
        border-bottom-right-radius: 4px;
    }
    .btn-group .form-horizontal .btn[type="submit"] {
        border-top-left-radius: 4px;
        border-bottom-left-radius: 4px;
    }
    .form-horizontal .form-group {
        margin-left: 0;
        margin-right: 0;
    }
    .form-group .form-control:last-child {
        border-top-left-radius: 4px;
        border-bottom-left-radius: 4px;
    }
    
    @media screen and (min-width: 768px) {
        #adv-search {
            width: 600px;
            margin: 0 auto;
        }
        .dropdown.dropdown-lg {
            position: static !important;
        }
        .dropdown.dropdown-lg .dropdown-menu {
            min-width: 300px;
        }
    }

    .secondary-dropdown-menu {
        margin-top: -1px;
        padding: 20px 20px;
        min-width: 300px; /* Minimum width */
        max-width: 300px; /* Maximum width */
    }
</style>