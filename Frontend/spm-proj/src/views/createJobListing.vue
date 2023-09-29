<template>

    <div class="createJobListing container my-5">
    <div class="text-center">
        <h1 class="">Create Job Listing</h1>
    </div>
    
    <hr>
        <div class="container">
            <div class="form-group">
                <label for="exampleInputEmail1">Name</label>
                <input type="email" class="form-control" id="jobName" aria-describedby="jobName" placeholder="Enter Job Listing Name">
                <!-- <small id="" class="form-text text-muted">This is a small description</small> -->
            </div>

            <label class="my-1 mr-2" for="inlineFormCustomSelectPref">Department</label>
            <select class="custom-select my-1 mr-sm-2 mb-4" id="inlineFormCustomSelectPref">
                <option selected>Choose Department...</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>

            <label for="exampleFormControlTextarea1">Job Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="6"></textarea>

            <!-- Checkboxes -->
            <div class="py-3">
                <label for="Skills">Skills Required</label><br>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
                    <label class="form-check-label" for="inlineCheckbox1">1</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">2</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3" disabled>
                    <label class="form-check-label" for="inlineCheckbox3">3 (disabled)</label>
                </div>
            </div>


            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>

    


</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'; // Import Bootstrap 4 CSS
import 'jquery/dist/jquery.min.js'; // Import jQuery
import 'bootstrap/dist/js/bootstrap.min.js'; // Import Bootstrap 4 JS

export default {
    name: 'createJobListing',
    // Other component options and code
};
</script>



<style>
/* Add your component-specific styles here */
/* .createJobListing {
    text-align: center;
    padding: 20px;
} */

/* Additional styling for elements on this page */
</style>