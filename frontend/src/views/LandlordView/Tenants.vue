<template>
  <div class="home">
    <div class="columns is-multiline">
      <div class="column is-12">
      </div>

      <div class="tenant-container">
        <div v-for="tenant in tenants" :key="tenant.user.id">
          <UserProfile v-bind:profile="tenant"></UserProfile>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import LoggedInNavbar from '@/components/LoggedInNavbar.vue'
import UserProfile from '@/components/UserProfile.vue';
import LandlordNav from '@/components/Landlord/LandlordNav.vue';
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';

export default {
  name: 'Tenants',
  data() {
    return {
      tenants: [],
      filterVisible: false,
    }
  },
  components: {
    LoggedInNavbar,
    UserProfile,
    LandlordNav,
    LandlordSubNav
},
  mounted() {
    this.getTenants()
    document.title = 'Tenants | The Perfect Landlord'
    localStorage.setItem("pageType", "landlord")
  },
  methods: {
    showFilter() {
          this.filterVisible = !this.filterVisible;
    },
    async getTenants() {
      const config = {'Authorization': 'Token d8b19cf836fcdd3ce64b776a1de6f3600164a329'}

      await axios
        .get('/landlord/tenants/', config)
        .then(response => {
          console.log(response.data)
          this.tenants = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>

*{
    text-decoration: none;
}
.tenant-container{
    display: flex;
    align-content: space-around;
    padding: 10px;
    width:max-content;
    height: max-content;
    text-decoration: none;
    flex: 0 0 192px;
}
.tenant{
    text-decoration: none;
    border: 2px solid black;
    padding: 20px;
    margin: 15px;
    display: flex;
    align-content: space-between;

}
.tenant:hover{
    background:whitesmoke;
    border-radius: 10px;
    font-size: 1.05em;
}
.tenant a{
    text-decoration: none;
    color: black;
}
.image,.details{
    padding: 5px;
    text-decoration: none;
}
img{
    width: 100px;
    height: 100px;
}
</style>
