<template>
    <TenantSubNav/>
    <div class="page-property">
        <div class="address-heading">
            <h1 class="address">{{property.address}}</h1>
        </div>

        <div class="main-section">
            <div clas="section1">
                <div class="img-section">
                    <figure @click="changeImage">
                        <img v-bind:src="property.get_image" class="main-image">                    
                    </figure>
                </div>
            </div>
            <div class="section2">
                <div class="sub-section-a">
                    <p><strong><i class="fas fa-dollar-sign"></i> Price: </strong>{{property.price}}/week</p>
                    <p> <strong>About Property: </strong>{{ property.description }}</p>
                </div>
                <div class="sub-section-b">
                    <button class="applyBtn" @click="generateForm">Apply</button>
                </div>
            </div>
        </div>
        <label> Essentials <i class="fas fa-arrow-down"></i></label>
        <div class="advants">
            <div>
              <span>Bedrooms</span>
              <div><i class="fas fa-th-large"></i><span>{{ property.room }}</span></div>
            </div>
            <div>
              <span>Bathrooms </span>
              <div><i class="fas fa-shower"></i><span>{{ property.bathroom }}</span></div>
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
                <div><i class="fas fa-snowflake"></i>
                    <span v-if="property.airConditioning == 1">Yes</span>
                    <span v-else-if="property.airConditioning == 0">No</span>
                </div>
              </div>
              <div>
                <span>Pool </span>
                <div><i class="fas fa-swimming"></i>
                    <span v-if="property.pool == 1">Yes</span>
                    <span v-else-if="property.pool == 0">No</span>
                </div>
              </div>
              <div>
                <span>Gym </span>
                <div><i class="fas fa-dumbbell"></i>
                    <span v-if="property.gym == 1">Yes</span>
                    <span v-else-if="property.gym == 0">No</span>
                </div>
              </div>
            </div>
    </div>
</template>

<script>
import LandingNavbar from '@/components/LandingNavbar.vue'
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';
import TenantSubNav from '@/components/Tenant/TenantSubNav.vue';
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

        generateForm(){
            this.$router.push('/application-form')
        },

        async getProperty() {
            this.$store.commit("setIsLoading", true);

            // Set logged in user token as header
            const config = {'Authorization': `Token ${localStorage.getItem("token")}`} 

            // Retrieve property unique slug 
            const property_slug = this.$route.params.property_slug;

            // Query property details
            await axios
                .get(`v2/property/properties/${property_slug}/`)
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
    components: { LandingNavbar, LandlordSubNav, TenantSubNav }
}

</script>

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
    .main-image{
        width: 65%;
        height: 65%;
    }
    img .thumbnail{
        width: 150vw;
        height: 100vh;
        
    }
    .main-section{
        display: block;
        justify-content:space-around;
        margin: 20px;
        padding: 25px;
    }
    .section1{
        padding: 25px;
        margin: 5px;
        display: flex;
         
    }
    .section2{
        padding: 5px;
        font-size: 1.5em;
        margin: 5px;
        display: flex;
        justify-content: space-between;
    }
    .advants{
        background-color: beige;
        padding: 20px;
        margin: 20px;
    }
    .applyBtn{
        background-color: maroon;
        padding: 5px;
        margin-top: 15px;
        border: none;
        border-radius: 2px;
        box-shadow: 0 0 1px;
        font-style: bold;
        font-size: 0.8em;
    }
    .applyBtn:hover{
        border: 2px solid black;
        transition: ease-in 0.35s;
        color: white;

    }
</style>
