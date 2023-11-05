<!-- Beat -->

<!-- Template -->
<template>
    
    <!-- Start of Content -->
    <div class="container-fluid colWidth">
        <div class="row align-items-center justify-content-center"> 

            <!-- Pending Requests -->
            <div class="colWidth">
                <h1 class="text-start">Pending Requests</h1>
                <div class="container-fluid w-100 p-0">
                    <div class="row rounded bg-secondary-subtle w-100 py-2 mx-0 my-2 justify-content-center"
                    v-for="application in applications" :key="application.application_id"
                    >
                    <v-col class="col-3">
                        <!-- <img :src="application.gameData.img"> -->
                    </v-col>

                    <v-col class="col-6">

                        {{ application.gameData.name }}
                    </v-col>
                    
                    <v-col class="col-3">
                        <!-- Each application is a form  -->
                        <form class="row g-3 justify-content-end align-items-center" id="approveRequest">
                            <input type="hidden" :value="application.application_id">
                            <button type="submit" class="btn btn-success w-auto"
                            @click="updateApplication()"
                            >Approve</button>
                            <button type="submit" class="btn btn-danger w-auto ms-1"
                            @click="updateApplication()"
                            >Reject</button>
                        </form>
                    </v-col>

                    </div>
                </div>
            </div>
            
        </div>

        <div class="row justify-content-center">
            <div class="col colWidth">
                <h1 class="text-start">Reviews</h1>
                <div class="container-fluid w-100 p-0">
                    <div class="row rounded bg-secondary-subtle w-100 py-2 mx-0 my-2 justify-content-center"
                    v-for="reviewInfo in reviews" :key="reviewInfo.name"
                    >
                        <div class="col-9">
                            <h4 class="text-start mb-0">{{ reviewInfo.title }}</h4> 
                            <p class="text-start text-body-secondary subtext my-0">{{ reviewInfo.name }}</p>
                        </div>
                        <div class="col-3">
                            <img src="../assets/star.png" class="star float-end" alt=""
                            v-for="n in reviewInfo.rating"
                            :key="n"
                            >
                        </div>
                        <p class="text-start my-1">{{ reviewInfo.review }}</p>
                        <p class="text-end text-body-secondary subtext m-0">Posted on: {{ reviewInfo.date }}</p>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>


<!-- Script -->
<script>
// Connection to Firebase
import { ref, onMounted } from 'vue'; // Import Vue composition API functions
import { app } from "../firebase/firebase";
import { getDatabase, ref as dbRef, get } from 'firebase/database';
import axios from 'axios';
import { getStorage, ref as storageRef, getDownloadURL } from 'firebase/storage';
import $ from 'jquery';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

const firebaseDatabaseURL = 'https://wad2-proj-642be-default-rtdb.asia-southeast1.firebasedatabase.app/';
const path = '/games.json'; // Replace with the path to your data
const applicationsPath = '/borrowApplications.json'



export default {
    setup() {
        const firebaseData = ref(null);

        onMounted(async () => {
        try {
            const db = getDatabase(app);
            const databaseRef = dbRef(db, 'games');

            const snapshot = await get(databaseRef);

            if (snapshot.exists()) {
            const data = snapshot.val();
            firebaseData.value = data; // Update the data property with fetched data
            } else {
            console.log('No data available');
            }
        } catch (error) {
            console.error('Error reading data from Realtime Database:', error);
        }
        });

        return {
        firebaseData,
        };
    },

    data(){
        return{
        applications: [],        
        reviews: [{
            title: "Great Game! Would Recommend!",
            name: "Dudette McReview",
            review: "I love this game! It's so fun! Played with my friends and we had a blast! Would recommend!",
            rating: 5,
            date: "2022-10-01",
        },
        {
            title: "Its alright, so so only :)",
            name: "Daniella YF",
            review: "The game is not in that great condition, and the cards are yellowing a little so we could tell what card each person held based on the condition. But overall, it was a fun game to play with my friends!",
            rating: 3,
            date: "2021-03-23",
        },
        ]
        }
    },

    methods: {
        getGameData() {
            
        },

        borrowGame(listing) {
            console.log(listing);
            this.$router.push({ name: 'borrowGame', params: { gameID: listing.id } });
        },

        async getApplicationsData() {
            await axios
            .get(firebaseDatabaseURL + applicationsPath)
            .then((response) => {
                
                // initiate application data 
                for (let app in response.data) {
                    this.applications.push(response.data[app]);
                }

                // add in the game data for each application
                for (let app in this.applications) {

                    axios
                    .get(firebaseDatabaseURL + path)
                    .then((response) => {
                    if (typeof response.data === 'object') {
                        let returnListing = response.data[this.applications[app].gameID];
                        // Initialize Firebase Storage
                        const storage = getStorage();                
                        if (Object.prototype.hasOwnProperty.call(returnListing, "img")) {
                            if (returnListing.img) {
                            const imageRef = storageRef(storage, returnListing.img);
                            getDownloadURL(imageRef)
                                .then((url) => {
                                // Update the 'img' property of the listing with the new URL
                                returnListing.img = url;
                                })
                                .catch((error) => {
                                console.error('Error getting download URL for image:', error);
                                });
                            }
                        }
                    
                        this.applications[app].gameData = returnListing;
                    } else {
                        console.error('Response data is not an object:', response.data);
                    }
                    })
                    .catch((error) => {
                    console.error('Error fetching data:', error);
                    });
                }
                console.log(this.applications)
                
            })
            .catch((error) => {
            console.error('Error fetching applications data:', error);
            });
        }

    },

    created() {
        this.getGameData();
        
    },

    mounted() {
    // Initialize the carousel when the component is mounted
    $('#gameCarousel');
    this.getApplicationsData();
  },
};
  
</script>


<!-- Style -->
<style>
    .bolded {
        font-weight: bold;
    }

    .subtext {
        font-size: 0.8rem;
    }

    .star {
        width: 20%;
        max-width: 25px;
        /* min-width: 15px; */
        height: auto;
    }

    .colWidth {
        width: 100%;
        max-width: 800px;
    }
</style>
