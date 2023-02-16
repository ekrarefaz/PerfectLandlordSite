<template>
    <div class="home">
      <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-2 has-text-centered">View Possible Tenants' profile:</h2>
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
  