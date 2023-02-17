<template>
  <div class="home">
    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">View Possible Tenants' profile:</h2>
      </div>

      <div class="tenant-container">
        <div v-for="tenant in tenants" :key="tenant.id">
            <router-link to="/">
            <div class="tenant">
                <div class="image">
                    <img src="../assets/logo.png" alt="">
                </div>
                <div class="details">
                    <h3>{{tenant.name}} ({{tenant.age}})</h3>
                    <sub>{{tenant.bio}}</sub>
                    <br>
                    <!--
                    <p>{{tenant.job}}</p>
                    <p>Preference: {{tenant.preference.type}}</p>
                    -->      
                </div>
            </div>
            </router-link>
        </div>
      </div>

      <div class="box" v-for="tenant in tenants">
        <!-- <figure class="image mb-4">
          <img :src="property.get_thumbnail">
        </figure> -->

        <!-- <h3>
          <div class="is-size-4">{{ tenant.name }}</div>
        </h3> -->

        <p>{{ tenant.bio }}</p>

        <!-- <router-link v-bind:to="tenant.get_absolute_url" class="button is-dark mt-4">View details</router-link> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import LoggedInNavbar from '@/components/LoggedInNavbar.vue'

import TenantFilter from '../components/Filters/TenantFilter.vue';


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
        .get('/tenants/', config)
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
