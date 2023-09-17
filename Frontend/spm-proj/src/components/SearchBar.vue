<template>
    <div class="container">
    <div class="row">
        <div class="col-md-12">
        <!-- Your Bootstrap search bar HTML here -->
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
                                    <select class="select" multiple data-mdb-placeholder="Example placeholder">
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
</template>
    
<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

export default {
    name: 'SearchBar',
};
</script>

<style>
/* Add component-specific styles here */
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
