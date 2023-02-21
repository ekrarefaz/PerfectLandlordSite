<template>
  <div class="home">
    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">View Possible Tenants' profile:</h2>
      </div>

      <UserProfile 
        v-for="tenant in tenants"
        v-bind:key="tenant.user.id"
        v-bind:profile="tenant" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import LoggedInNavbar from '@/components/LoggedInNavbar.vue'

import UserProfile from '@/components/UserProfile.vue';


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
    UserProfile
},
  mounted() {
    this.getTenants()
    document.title = 'Tenants | The Perfect Landlord'
  },
  methods: {
    showFilter() {
          this.filterVisible = !this.filterVisible;
    },
    async getTenants() {
      const config = {'Authorization': 'Token 01ff9afdd60b6d23b92b5eed55dd87831a30bc9c'}

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
