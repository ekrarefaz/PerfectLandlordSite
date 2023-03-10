<template>
  <div class="topbar">
    <div class="searchBar" v-show="!filterVisible">
      <form method="get" action="/properties">
        <input id="searchQueryInput" type="text" name="query" placeholder="Search"/>

        <button id="searchQuerySubmit" type="submit" @click="searchQuery">
          <svg style="width:24px;height:24px" viewBox="0 0 24 24"><path fill="#666666" d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
          </svg>
        </button>
      </form>
    </div>
    <i class="fas fa-filter filterIcon" @click="showFilter" v-show="!filterVisible">Filter</i>
    <div v-show="filterVisible" class="filter">
      <PropertyFilter/>
    </div>
  </div>
  <div v-if="!filterVisible">
    <div class="container">
      <div class="box" v-for="property in properties">
        <router-link v-bind:to="'properties'+ property.get_absolute_url">
          <div class="top">
            <img :src="property.get_thumbnail" alt="thumbnail" />
          </div>
        </router-link>
        <div class="bottom">
          <h3>{{property.address}}</h3>
          <span>
            <i class="fas fa-star" @click="saveProperty"></i>
          </span>
          <p>
            {{ property.description }}
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


<script>
import axios from 'axios'

import PropertyBox from '@/components/Tenant/PropertyBox'
import PropertyFilter from '@/components/Filters/PropertyFilter.vue'
import LandlordProfile from '../LandlordView/LandlordProfile.vue'
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue'
import SearchBar from '@/components/Filters/SearchBar.vue'

export default {
  name: 'Home',
  data() {
    return {
      properties: [],
      filterVisible: false,
      saved: false,
      query: ''
    }
  },
  components: {
    PropertyBox,
    PropertyFilter,
    LandlordProfile,
    LandlordSubNav,
    SearchBar,
  },
  mounted() {
    document.title = 'My Properties | The Perfect Landlord'
    localStorage.setItem("pageType", "tenant")

    // Get search query
    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if (params.get('query')) {
        this.query = params.get('query')

        this.searchQuery()
    }
    else {
      this.getProperties()
    }
  },  
  methods: {
    showFilter(){
            this.filterVisible = !this.filterVisible
    },
    saveProperty(){
      this.saved = !this.saved
    },
    async getProperties() {      
      // Print request
      axios.interceptors.request.use(request => {
        console.log('Starting Request', JSON.stringify(request, null, 2))
        return request
      })

      // Request
      await axios
        .get('v2/property/properties/')
        .then(response => {
          console.log(response.data)
          this.properties = response.data
        })
        .catch(error => {
          console.log(error)
        }); 
      
    },
    async searchQuery(){    
      const data = {
          'query': this.query
      }

      // Search properties by address
      await axios
          .post('v2/property/search/', data)
          .then(response => {
            console.log(response.data)

            // Store filtered properties in data
            this.properties = response.data
          })
  }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

.container {
  width: 1100px;
  margin: 30px;
  display: flex;
  justify-content: space-between;
  padding-left: 0px;
  flex-wrap: wrap;
}


.container .box {
  width: calc((100% / 3) - 20px);
  background-color: white;
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
.filterIcon{
  float: right;
  margin: 30px;
}

/* Searchbar */
.searchBar {
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    
#searchQueryInput {
    width: 100%;
    height: 2.8rem;
    background: #f5f5f5;
    outline: none;
    border: none;
    border-radius: 1.625rem;
    padding: 0 3.5rem 0 1.5rem;
    font-size: 1rem;
}

#searchQuerySubmit {
    width: 3.5rem;
    height: 2.8rem;
    margin-left: -3.5rem;
    background: none;
    border: none;
    outline: none;
}

#searchQuerySubmit:hover {
    cursor: pointer;
}
</style>