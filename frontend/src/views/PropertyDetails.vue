<template>
    <div class="page-property">
        <div class="address-heading">
            <h1 class="address">{{ property.address }}</h1>
        </div>
        <div class="main-section">
            <div clas="section1">
                <figure>
                    <img v-bind:src="property.get_image">
                </figure>
            </div>
            <div class="section2">
                <p><strong>Price: </strong>${{ property.price }}/week</p>
                <p>{{property.description}}</p>
            </div>
        </div>
        <div class="feature-section">

        </div>
    </div>
</template>

<style scoped>
    .address-heading{
        font-size: 4em;
        text-align: center;
    }
    img{
        width: 50%;
        height: 50%;
    }
    .main-section{
        display: flex;
        justify-content: space-around;
        margin: 20px;
        border: 2px solid black;
        padding: 25px;
    }
    .section1{
        border: 1px solid black;
        padding: 25px;
    }
    .section2{
        border: 1px solid black;
        padding: 25px;
    }
</style>

<script>
import LandingNavbar from '@/components/LandingNavbar.vue'
import axios from 'axios'

export default {
    name: "Property",
    data() {
        return {
            property: {},
        };
    },
    mounted() {
        this.getProperty();
    },
    methods: {
        async getProperty() {
            this.$store.commit("setIsLoading", true);
            const property_slug = this.$route.params.property_slug;
            await axios
                .get(`/properties/${property_slug}`)
                .then(response => {
                console.log(response.data);
                this.property = response.data;
                document.title = this.property.address + " | The Perfect Landlord";
            })
                .catch(error => {
                console.log(error);
            });
            this.$store.commit("setIsLoading", false);
        },
    },
    components: { LandingNavbar }
}
</script>