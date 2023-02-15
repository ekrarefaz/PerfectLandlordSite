<template>
    <div class="page-property">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="property.get_image">
                </figure>

                <h1 class="address">{{ property.address }}</h1>

                <p>{{ property.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>${{ property.price }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Property',
    data() {
        return {
            property: {},
        }
    },
    mounted() {
        this.getProperty() 
    },
    methods: {
        async getProperty() {
            this.$store.commit('setIsLoading', true)

            const property_slug = this.$route.params.property_slug

            await axios
                .get(`/properties/${property_slug}`)
                .then(response => {
                    console.log(response.data)
                    this.property = response.data

                    document.title = this.property.address + ' | The Perfect Landlord'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
            },
    }
}
</script>