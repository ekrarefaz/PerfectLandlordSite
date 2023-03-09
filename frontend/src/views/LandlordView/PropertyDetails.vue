<template>
    <LandlordSubNav/>
        <div class="page-property">
            <div class="address-heading">
                <h1 class="address">{{property.address}}</h1>
                <i class="fas fa-pen" @click="makeEditableForm" v-show="!editable"></i>
                <i class="fas fa-print" @click="saveUpdates" v-show="editable"></i>

            </div>
    
            <div class="main-section">
                <div clas="section1">
                    <div class="img-section">
                        <figure @click="changeImage">
                            <img v-bind:src="property.get_image" v-show="image" class="main-image">
                            <img v-bind:src="property.get_thumbnail" v-show="!image" class="thumbnail">
                        </figure>
                    </div>
                </div>
                <div class="section2">
                    <p> <strong>Price: </strong>
                        <span v-show="!editable" class="strong">
                            {{ property.price}}<em>/Week</em>
                        </span>
                        <span v-show="editable">
                            <input type="text" v-model="propertyPrice">
                        </span>
                    </p>
                    <p> <strong>About: </strong>
                        <span v-show="!editable" class="strong">
                            {{ property.description }}
                        </span>
                        <span v-show="editable">
                            <input type="text" v-model="propertyBio">
                        </span>
                    </p>
                </div>
            </div>
            <label> Essentials <i class="fas fa-arrow-down"></i></label>
            <div class="advants">
                <div>
                    <span v-show="!editable" class="strong">
                        <span>Bedrooms</span>
                        <div><i class="fas fa-th-large"></i><span>{{property.room}}</span></div>
                    </span>
                    <span v-show="editable">
                        <input type="number" v-model="propertyRoom">
                    </span>
                </div>
                <div>
                    <span v-show="!editable" class="strong">
                        <span>Bathrooms </span>
                        <div><i class="fas fa-shower"></i><span>{{property.bathroom}}</span></div>
                    </span>
                    <span v-show="editable">
                        <input type="number" v-model="propertyBath">
                    </span>
                </div>
                <div>
                    <span v-show="!editable" class="strong">
                        <span>Type </span>
                        <div>
                          <i class="fas fa-vector-square"></i><span>{{property.type}}</span>
                        </div>
                    </span>
                    <span v-show="editable">
                        <input type="text" v-model="propertyType">
                    </span>
                </div>
              </div>

              <label> Features <i class="fas fa-arrow-down"></i></label>
              <div class="advants features">
                <div>
                  <span>AirCon</span>
                  <div v-show="!editable"><i class="fas fa-snowflake"></i>
                      <span v-if="property.airConditioning == 1">Yes</span>
                      <span v-else-if="property.airConditioning == 0">No</span>
                  </div>
                  <div v-show="editable">
                    <select v-model="property.airConditioning">
                        <option value=1>Yes</option>
                        <option value=0>No</option>
                      </select>
                  </div>
                </div>
                <div>
                  <span>Pool </span>
                  <div v-show="!editable"><i class="fas fa-swimming"></i>
                      <span v-if="property.pool == 1">Yes</span>
                      <span v-else-if="property.pool == 0">No</span>
                  </div>
                  <div v-show="editable">
                    <select v-model="property.pool">
                        <option value=1>Yes</option>
                        <option value=0>No</option>
                      </select>
                  </div>
                </div>
                <div>
                  <span>Gym </span>
                  <div v-show="!editable"><i class="fas fa-dumbbell"></i>
                      <span v-if="property.gym == 1">Yes</span>
                      <span v-else-if="property.gym == 0">No</span>
                  </div>
                  <div v-show="editable">
                    <select v-model="property.gym">
                        <option value=1>Yes</option>
                        <option value=0>No</option>
                      </select>
                  </div>
                </div>
              </div>
        </div>
</template>

<script>
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';

import axios from 'axios'
    export default{
        data(){
            return{
                property: [],
                editable: false,
                propertyPrice: 550,
                propertyBio: "This charming two-story home boasts three bedrooms, two and a half bathrooms, and a spacious living room that's perfect for entertaining guests. The kitchen features modern appliances and plenty of counter space for preparing delicious meals.",
                propertyType: "Apartment",
                propertyRoom: 3,
                propertyBath: 2,
                propertyAirCon: 1,
                propertyPool: 0,
                propertyGym: 1
            }
        },
        components:{
            LandlordSubNav
        },
        mounted(){
                this.getProperty()
        },
        methods:{
            makeEditableForm(){
                this.editable = true
            },
            saveUpdates(){
                this.editable = false
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
        }
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
