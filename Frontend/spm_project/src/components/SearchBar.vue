<template>
      <div class="input-group" id="adv-search">
            <input type="text" class="form-control" placeholder="Search for job listings" />
            <div class="input-group-btn">
                  <div class="btn-group" role="group">
                        <div class="dropdown dropdown-lg">
                              <button type="button" class="btn btn-default dropdown-toggle border-bottom border-top"
                                    data-toggle="dropdown" aria-expanded="false">
                                    <span class="caret"></span>
                              </button>
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
                                                <input class="form-control" type="text" placeholder="Use ; as separator" />
                                          </div>

                                          <!-- Add your skill selection dropdown here -->

                                          <button type="button" class="btn btn-outline-primary">
                                                <i class="bi bi-search"></i> Search
                                          </button>
                                    </form>
                              </div>
                        </div>
                  </div>
            </div>
      </div>
</template>
    
<script>
export default {
      // Component logic here
};
</script>
    
<style>
/* Component-specific styles here */
</style>