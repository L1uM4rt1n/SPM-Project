<template>
  <!-- <div>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div> -->
  <div>
    <AppNavbar />
    <SearchBar />
    <JobListings />
  </div>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

// export default {
//   name: 'App',
//   components: {
//     HelloWorld
//   }
// }
import AppNavbar from './components/AppNavbar.vue';
import SearchBar from './components/SearchBar.vue';
import JobListings from './components/JobListings.vue';

export default {
  components: {
    AppNavbar,
    SearchBar,
    JobListings,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
