<template>
    <div class="page-tenant">
        <div class="main-section">
            <div clas="section1">
                <div class="img-section">
                    <figure @click="changeImage">
                        <img src="@/assets/elon.jpg" class="main-image">                    
                    </figure>
                </div>
            </div>
            <div class="section2">
                <div class="sub-section-a">
                    <p><strong>Name: </strong>{{name}}</p>
                    <p> <strong>Bio: </strong>I have money</p>
                </div>
            </div>
        </div>
        <div class="detail-section">
        <label>
             <Details>
                <p><strong>Email: </strong>tenant@mail.com</p>
                <p><strong>DOB: </strong>11/11/11</p>
                <p><strong>Location: </strong>Melbourne</p>

            </Details> 
        </label>
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
            tenants:[],
            tenant:[],
            image: false,
            name: this.name,
        };
    },
    props:['name'],
    mounted() {
        this.getTenants()
    },
    methods: {

    async getTenants() {
      const config = {'Authorization': `Token ${localStorage.getItem("token")}`}  

      await axios
        .get('v2/user/tenants', config)
        .then(response => {
          console.log(response.data)
          this.tenants = response.data
          this.getTenantDetails(this.name)
        })
        .catch(error => {
          console.log(error)
        })
    },
    getTenantDetails(name){
        for(var tenant in this.tenants){
            if(tenant.user.id == this.name){
                console.log("Okay")
            }
            else{
                console.log("None")
            }
        }
    }
    },

    components: { LandingNavbar, LandlordSubNav }
}

</script>

<style scoped>

    .main-image{
        width: 45%;
        height: 45%;
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
</style>
