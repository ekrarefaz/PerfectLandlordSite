<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to The Perfect Landlord
            </p>
            <p class="subtitle">
                This is where....
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">My Properties:</h2>
      </div>

      <div class="box" v-for="property in myProperties">
        <figure class="image mb-4">
          <img :src="property.get_thumbnail">
        </figure>

        <h3>
          <div class="is-size-4">{{ property.address }}</div>
        </h3>

        <p>${{ property.price }}/Week</p>

        <router-link v-bind:to="property.get_absolute_url" class="button is-dark mt-4">View details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import PropertyBox from '@/components/PropertyBox'

export default {
  name: 'Home',
  data() {
    return {
      myProperties: []
    }
  },
  components: {
    PropertyBox
  },
  mounted() {
    this.getMyProperties()
    document.title = 'Home | Djackets'
  },
  methods: {
    async getMyProperties() {
      const config = {'Authorization': 'Token 01ff9afdd60b6d23b92b5eed55dd87831a30bc9c'}

      await axios
        .get('/properties/', config)
        .then(response => {
          console.log(response.data[0])
          this.myProperties = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
