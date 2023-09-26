<template>
    <SearchBar> </SearchBar>
    <div>
      <h1 class="pb-3">Role Listings</h1>
      <div class="row d-flex mx-2">
        <ItemCard v-for="listing in this.filteredListings" :listingData="listing"
          v-if="filteredListings && filteredListings.length > 0" :uid="user_id" />
        <div class="container-fluid d-flex justify-content-center align-items-center"
          style="height: calc(100vh - 200px); overflow: hidden;" v-else-if="searchInput">
          <p class="fs-5" style="color: #C6C6C6">No results found.</p>
        </div>
        <ItemCard v-for="listing in this.listings" :listingData="listing" v-else :uid="user_id" />
      </div>
    </div>

</template>

<script>
import SearchBar from '@/components/SearchBar'

export default {
  components : {
    SearchBar
  }
}

</script>