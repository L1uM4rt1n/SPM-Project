<template>
  <div class="container p-5">
    <!-- SEARCH BAR -->
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <form class="d-flex">
            <input class="form-control me-1" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" :aria-controls="'collapseExample'">
              <i class="fa-solid fa-filter"></i>
            </button>
            <button class="btn btn-outline-primary" type="submit">
              <i class="fa-solid fa-magnifying-glass"></i>
            </button>
          </form>
          <div class="collapse" id="collapseExample">
            <form>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Filter by</label>
                <select class="form-select" aria-label="Default select example">
                  <option selected>All Departments</option>
                  <option value="1">Finance</option>
                  <option value="2">HR</option>
                  <option value="3">IT</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Author</label>
                <input type="text" class="form-control" placeholder="Author">
              </div>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Contain Skills</label>
                <input type="formtags" class="form-control" data-role="tagsinput" placeholder="Use ; as separator">
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      searchText: '',
      selectedDepartment: '0',
      skills: [],
      selectedSkills: [],
      selectAllSkills: false,
    };
  },
};
</script>

<style scoped>
.collapse {
  margin-top: 2em;
  padding: 5px 10px;
  border: 1px solid grey;
  border-radius: 10px;
  text-align: left;
}
</style>
