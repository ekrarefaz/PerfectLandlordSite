<template>
    <LandlordSubNav/>
        <div class="page-property">
            <div class="address-heading">
                <h1 class="address">8/3 Kooyonkoot Road</h1>
                <i class="fas fa-pen" @click="makeEditableForm" v-show="!editable"></i>
                <i class="fas fa-print" @click="saveUpdates" v-show="editable"></i>

            </div>
    
            <div class="main-section">
                <div clas="section1">
                    <div class="img-section">
                        <figure @click="changeImage">
                            <img src="@/assets/chris-robert--ryDtcapIas-unsplash.jpg" class="main-image">
                            <!-- <img v-bind:src="property.get_image" v-show="image" class="main-image">
                            <img v-bind:src="property.get_thumbnail" v-show="!image" class="thumbnail"> -->
                        </figure>
                    </div>
                </div>
                <div class="section2">
                    <p> <strong>Price: </strong>
                        <span v-show="!editable" class="strong">
                            {{ propertyPrice}}<em>/Week</em>
                        </span>
                        <span v-show="editable">
                            <input type="text" v-model="propertyPrice">
                        </span>
                    </p>
                    <p> <strong>About: </strong>
                        <span v-show="!editable" class="strong">
                            {{ propertyBio }}
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
                  <span>Bedrooms</span>
                  <div><i class="fas fa-th-large"></i><span>3</span></div>
                </div>
                <div>
                  <span>Bathrooms </span>
                  <div><i class="fas fa-shower"></i><span>2</span></div>
                </div>
                <div>
                  <span>Type </span>
                  <div>
                    <i class="fas fa-vector-square"></i
                    ><span>House</span>
                  </div>
                </div>
              </div>
              <label> Features <i class="fas fa-arrow-down"></i></label>
              <div class="advants features">
                  <div>
                    <span>AirCon</span>
                    <div><i class="fas fa-snowflake"></i><span>Yes</span></div>
                  </div>
                  <div>
                    <span>Pool </span>
                    <div><i class="fas fa-swimming"></i><span>No</span></div>
                  </div>
                  <div>
                    <span>Gym </span>
                    <div>
                      <i class="fas fa-dumbbell"></i
                      ><span>Yes</span>
                    </div>
                  </div>
                </div>
        </div>
</template>

<script>
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';

    export default{
        data(){
            return{
                editable: false,
                propertyPrice: 550,
                propertyBio: "This charming two-story home boasts three bedrooms, two and a half bathrooms, and a spacious living room that's perfect for entertaining guests. The kitchen features modern appliances and plenty of counter space for preparing delicious meals."
            }
        },
        components:{
            LandlordSubNav
        },
        methods:{
            makeEditableForm(){
                this.editable = true
            },
            saveUpdates(){
                this.editable = false
            }
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
