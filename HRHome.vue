<!-- import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue) -->

<!------------------------------------------------------- Template --------------------------------------------------->

<template>
        <!-- NAV BAR -->
        <nav class="navbar navbar-light bg-light">
            <div class="container-fluid">
            <a class="navbar-brand" href="#">
            <img src="/docs/4.3/assets/brand/bootstrap-solid.svg" width="30" height="30" alt="">
            </a>

            <a class="navbar-brand" href="#">
                <img src="/docs/4.3/assets/brand/bootstrap-solid.svg" width="30" height="30" alt="">
            </a>
            </div>
        </nav>
        <!-- NAV BAR -->

        <div class="container p-5">
            <!-- SEARCH BAR -->
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="input-group" id="adv-search">
                            <input type="text" class="form-control " placeholder="Search for job listings" />
                            <div class="input-group-btn">
                                <div class="btn-group" role="group">
                                    <div class="dropdown dropdown-lg">
                                        <button type="button" class="btn btn-default dropdown-toggle border-bottom border-top" data-toggle="dropdown" aria-expanded="false"><span class="caret"></span></button>
                                        <div class="dropdown-menu dropdown-menu-right" role="menu">
                                            <form class="form-horizontal" role="form">
                                                <div class="form-group">
                                                    <label for="filter">Filter by</label>
                                                    <select class="form-control">
                                                        <option value="0" selected>All departments</option>
                                                        <option value="1">IT</option>
                                                        <option value="2">Finance</option>
                                                        <option value="3">HR</option>
                                                        <option value="4">Marketing</option>
                                                    </select>
                                                </div>
                                                <div class="form-group">
                                                    <label for="contain">Author</label>
                                                    <input class="form-control" type="text" />
                                                </div>
                                                <div class="form-group">
                                                    <label for="contain">Contains the skills</label>
                                                    <input class="form-control" type="text"  placeholder ="Use ; as separator"/>
                                                </div>

                                                <div class="form-group dropdown">
                                                    <select class="select" multiple data-mdb-placeholder="Example placeholder" multiple>
                                                        <option value="1">One</option>
                                                        <option value="2">Two</option>
                                                        <option value="3">Three</option>
                                                        <option value="4">Four</option>
                                                        <option value="5">Five</option>
                                                    </select>
                                                </div>

                                                <div class="dropdown" data-control="checkbox-dropdown">
                                                    <label class="dropdown-label"><b>Select Skills</b></label>
                                                    
                                                    <div class="dropdown-list">
                                                        <a href="#" data-toggle="check-all" class="dropdown-option">
                                                            Check All  
                                                        </a>
                                                        
                                                        <label class="dropdown-option">
                                                            <input type="checkbox" name="dropdown-group" value="Selection 1" />
                                                            Web development
                                                        </label>
                                                        
                                                        <label class="dropdown-option">
                                                            <input type="checkbox" name="dropdown-group" value="Selection 2" />
                                                            Excel
                                                        </label>
                                                        
                                                        <label class="dropdown-option">
                                                            <input type="checkbox" name="dropdown-group" value="Selection 3" />
                                                            Python
                                                        </label>
                                                        
                                                        <label class="dropdown-option">
                                                            <input type="checkbox" name="dropdown-group" value="Selection 4" />
                                                            Powerpoint
                                                        </label>
                                                        
                                                        <label class="dropdown-option">
                                                            <input type="checkbox" name="dropdown-group" value="Selection 5" />
                                                            Java
                                                        </label>      
                                                        </div>
                                                    </div>
                                        
                                            </form>
                                        </div>
                                    </div>
                                    <button type="button" class="btn btn-outline-primary">
                                        <i class="bi bi-search"></i> Search
                                    </button>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div> <!-- END OF SEARCH BAR -->

            <div class="container">   <!-- Biggest container -->

            <div class="container"> <!-- Display Ttile and Creating listing button -->

                <h1 class="text-center">Job Listings</h1>

                <div class="d-flex flex-row justify-content-end p-1">

                <!-- Create Job Listing Button -->
                    <a class="btn btn-primary" href="#" role="button">Create Job Listing</a>
                </div> <!-- Display Ttile and Creating listing button -->
            </div>


            <div class="container"> <!-- Container containing cards -->
                
                <div class="card"> <!-- Card Listing -->
                    <div class="card-body">
                        <h5 class="card-title">Software Developer</h5>
                        <p class="card-text">Skills: You need to be able to code.</p>
                        <div class="d-flex justify-content-end mb-auto float">
                            <a href="#" class="btn">Edit</a>
                        </div>
                    </div>
                </div> <!-- End of Card representing each listing -->

                <div class="card"> <!-- Card Listing -->
                    <div class="card-body">
                        <h5 class="card-title">Finance Executive</h5>
                        <p class="card-text">Skills: You need to be able to code.</p>
                        <div class="d-flex justify-content-end mb-auto float">
                            <a href="#" class="btn">Edit</a>
                        </div>
                    </div>
                </div> <!-- End of Card representing each listing -->
                
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Engineer</h5>
                        <p class="card-text">Skills: You need to be able to code.</p>
                        <div class="d-flex justify-content-end mb-auto float">
                            <a href="#" class="btn">Edit</a>
                        </div>
                    </div>
                </div> <!-- End of Card representing each listing -->
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Software Developer</h5>
                        <p class="card-text">Skills: You need to be able to code.</p>
                        <div class="d-flex justify-content-end mb-auto float">
                            <a href="#" class="btn">Edit</a>
                        </div>
                    </div>
                </div> <!-- End of Card representing each listing -->
            </div>
        </div>
        </div> <!-- END OF BIGGEST CONTAINER DIV -->

</template>


<!------------------------------------------------------- Script --------------------------------------------------->
<script>
</script>


<!------------------------------------------------------- Style --------------------------------------------------->
<style scoped>
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
            width: 500px;
            margin: 0 auto;
        }
        .dropdown.dropdown-lg {
            position: static !important;
        }
        .dropdown.dropdown-lg .dropdown-menu {
            min-width: 500px;
        }
    }
</style>