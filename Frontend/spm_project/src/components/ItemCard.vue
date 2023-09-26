<template>
    <router-link
    ::to="{ path: '/roleinfo', query: { listingID: listingData.listingid} }"
    style="text-decoration: none; color: inherit;">
    <div class="card">
        <div class="card-header">
          Featured
        </div>
        <div class="card-body">
          <h5 class="card-title">Special title treatment</h5>
          <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
    </div>   
    </router-link>
</template>

<script>
    export default {
    name: 'ItemCard',
    props: {
        listingData: null,
        mylistings: {
        type: Boolean,
        default: false
        }
    }
</script>