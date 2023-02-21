<template>
    <div class="landlordNav">
        <LandlordNav/>
    </div>
    <div class="page-property">
        <div class="address-heading">
            <h1 class="address">{{ property.address }}</h1>
        </div>

        <div class="main-section">
            <div clas="section1">
                <figure @click="changeImage">
                    <img v-bind:src="property.get_image" v-show="image" class="main-image">
                    <img v-bind:src="property.get_thumbnail" v-show="!image" class="thumbnail">
                </figure>
            </div>
            <div class="section2">
                <p><strong><i class="fas fa-dollar-sign"></i> Price: </strong>{{ property.price }}/week</p>
                <p> <strong>About Property: </strong>{{property.description}}</p>
                <button class="applyBtn">Apply</button>
            </div>
        </div>
        <label> Essentials <i class="fas fa-arrow-down"></i></label>
        <div class="advants">
            <div>
              <span>Bedrooms</span>
              <div><i class="fas fa-th-large"></i><span>{{property.room}}</span></div>
            </div>
            <div>
              <span>Bathrooms </span>
              <div><i class="fas fa-shower"></i><span>{{property.bathroom}}</span></div>
            </div>
            <div>
              <span>Type </span>
              <div>
                <i class="fas fa-vector-square"></i
                ><span>{{property.type}}</span>
              </div>
            </div>
          </div>
          <label> Features <i class="fas fa-arrow-down"></i></label>
          <div class="advants features">
              <div>
                <span>AirCon</span>
                <div><i class="fas fa-snowflake"></i><span>{{property.airConditioning}}</span></div>
              </div>
              <div>
                <span>Pool </span>
                <div><i class="fas fa-swimming"></i><span>{{property.pool}}</span></div>
              </div>
              <div>
                <span>Gym </span>
                <div>
                  <i class="fas fa-dumbbell"></i
                  ><span>{{property.gym}}</span>
                </div>
              </div>
            </div>
    </div>
</template>

<style scoped>
    .landlordNav{
        justify-content: center;
    }
    .advants{
        display: flex;
        justify-content: space-around;
    }
    .advants:hover{
        color: maroon;
    }
    .address-heading{
        font-size: 3em;
        text-align: center;
        text-decoration: underline;
        margin: 30px;
        margin-top: 50px;
    }
    img .main-image{
        width: 85%;
        height: 85%;
    }
    img .thumbnail{
        width: 150vw;
        height: 100vh;
        
    }
    .main-section{
        display: flex;
        justify-content:space-evenly;
        margin: 20px;
        padding: 25px;
    }
    .section1{
        padding: 25px;
        margin: 5px;
         
    }
    .section2{
        padding: 5px;
        font-size: 1.5em;
        margin: 5px;
    }
    .advants{
        background-color: beige;
        padding: 20px;
        margin: 20px;
    }
    .applyBtn{
        padding: 5px;
        margin-top: 15px;
        border: none;
        border-radius: 2px;
        box-shadow: 0 0 1px;
        font-style: bold;
        font-size: 0.8em;
    }
    .applyBtn:hover{
        background-color: maroon;
        border: 2px solid black;
        transition: ease-in 0.35s;
        color: white;

    }
</style>

<script>
import LandingNavbar from '@/components/LandingNavbar.vue'
import LandlordNav from '@/components/Landlord/LandlordNav.vue';
import axios from 'axios'

export default {
    name: "Property",
    data() {
        return {
            property: {},
            timer: null,
            currentIndex: 0,
            image: false,
        };
    },
    mounted() {
        this.getProperty();
        if(this.property != null){
            this.startSlide();
        }
    },
    methods: {
        changeImage(){
            this.image = !this.image
        },
        startSlide: function() {
            this.timer = setInterval(this.next, 4000);
        },
        next: function() {
            this.currentIndex += 1;
        },
        prev: function() {
            this.currentIndex -= 1;
        },

        async getProperty() {
            this.$store.commit("setIsLoading", true);
            const property_slug = this.$route.params.property_slug;
            await axios
                .get(`/landlord/my-properties/${property_slug}`)
                .then(response => {
                console.log(response.data);
                this.property = response.data;
                document.title = this.property.address + " | The Perfect Landlord";
            })
                .catch(error => {
                console.log(error);
            });
            this.$store.commit("setIsLoading", false);
        },
    },
    computed:{
        currentImg: function() {
            return this.images[Math.abs(this.currentIndex) % this.images.length];
        },
    },
    components: { LandingNavbar, LandlordNav }
}

</script>