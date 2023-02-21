<template>
  <LandlordSubNav/>
  <div v-if="!filterVisible">
    <div class="container">
    <div class="box" v-for="property in myProperties">
      <router-link v-bind:to="property.get_absolute_url">
        <div class="top">
          <img :src="property.get_thumbnail" alt="thumbnail" />
          <span>
            <i class="fas fa-heart" @click="saveProperty"></i>
          </span>
        </div>
      </router-link>
      <div class="bottom">
        <h3>{{property.address}}</h3>
        <p>
          {{property.description}}
        </p>
        <div class="advants">
          <div>
            <span>Bedrooms</span>
            <div><i class="fas fa-th-large"></i><span>{{property.room}}</span></div>
          </div>
          <div>
            <span>Bathrooms</span>
            <div><i class="fas fa-shower"></i><span>{{property.bathroom}}</span></div>
          </div>
          <div>
            <span>Type</span>
            <div>
              <i class="fas fa-vector-square"></i
              ><span>{{property.type}}</span>
            </div>
          </div>
        </div>
        <div class="price">
          <span>For Rent</span>
          <span>${{property.price}}/week</span>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>
<style>
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
.filter
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: #eee;
}

.container {
  width: 1100px;
  margin: 30px auto;
  display: flex;
  justify-content: space-between;
  padding-left: 100px;
}

.container .box {
  width: calc((100% / 3) - 20px);
  background-color: white;
  position: relative;
}

.container .box:hover{
  color: maroon;
}

.container .box .top {
  position: relative;
  background-color: red;
}

.container .box .top:before {
  content: "";
  width: 100%;
  height: 100%;
  background-color: rgba(43, 187, 175, 0.829);
  position: absolute;
  left: 0;
  top: 0;
  transition: 0.3s;
  opacity: 0;
}

.container .box .top:hover:before {
  opacity: 1;
}

.container .box .top:after {
  content: "View Property";
  color: white;
  font-size: 12px;
  padding: 10px;
  border: 1px solid white;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  cursor: pointer;
  transition: 0.3s;
  opacity: 0;
}

.container .box .top:hover:after {
  opacity: 1;
}

.container .box .top img {
  width: 100%;
  margin-bottom: -4px;
}

.container .box .top span {
  position: absolute;
  right: 20px;
  bottom: 15px;
  color: white;
  font-size: 20px;
}

.container .box .top span i {
  margin-left: 5px;
}

.container .box .bottom {
  padding: 20px 15px;
  position: relative;
}

.container .box:not(:last-of-type) .bottom:before {
  content: "Hot";
  background-color: #ea723d;
  color: white;
  font-size: 11px;
  padding: 4px 7px;
  position: absolute;
  left: 20px;
  top: -40px;
  z-index: 1;
}

.container .box .bottom h3 {
  font-size: 25px;
}

.container .box .bottom > p {
  margin: 15px 0;
  font-size: 13px;
  line-height: 1.4;
  color: #777;
}

.container .box .bottom .advants {
  display: flex;
}

.container .box .bottom .advants > div {
  margin-right: 15px;
}

.container .box .bottom .advants > div > span {
  font-weight: bold;
  font-size: 12px;
}

.container .box .bottom .advants > div > div {
  margin-top: 10px;
  display: flex;
  align-items: center;
}

.container .box .bottom .advants > div > div i {
  color: #777;
  font-size: 22px;
}

.container .box .bottom .advants > div > div > span {
  font-size: 12px;
  font-weight: bold;
  margin-left: 10px;
}

.container .box .bottom .advants > div > div > span > span {
  color: #777;
  font-weight: normal;
  margin-left: 5px;
}

.container .box .bottom .price {
  margin-top: 20px;
}

.container .box .bottom .price span:first-of-type {
  display: block;
  font-size: 13px;
  font-weight: bold;
  margin-bottom: 5px;
}

.container .box .bottom .price span:last-of-type {
  color: #3eaba1;
  font-size: 22px;
}

button{
  padding: 10px;
  width: 50%;
  align-items: center;
  color: black;
  
}
</style>
<script>
import axios from 'axios'

import PropertyBox from '@/components/Tenant/PropertyBox'
import LoggedInNavbar from '@/components/LoggedInNavbar.vue'
import PropertyFilter from '@/components/Filters/PropertyFilter.vue'
import LandlordProfile from '../LandlordView/LandlordProfile.vue'
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue'

export default {
  name: 'Home',
  data() {
    return {
      myProperties: [],
      filterVisible: false,
    }
  },
  components: {
    PropertyBox,
    LoggedInNavbar,
    PropertyFilter,
    LandlordProfile,
    LandlordSubNav,
},
  mounted() {
    this.getMyProperties()
    document.title = 'My Properties | The Perfect Landlord'
  },
  methods: {
    showFilter(){
            this.filterVisible = !this.filterVisible
    },
    async getMyProperties() {
      const config = {'Authorization': 'Token 01ff9afdd60b6d23b92b5eed55dd87831a30bc9c'}

      await axios
        .get('/landlord/my-properties/', config)
        .then(response => {
          console.log(response.data[0])
          this.myProperties = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    
  }
}
</script>
