<template>
<<<<<<< HEAD
    <div v-show="loaded">
        <LoadingAnimated/>
    </div>
    <div v-show="!loaded">
        <HomePage/>
    </div>
=======
    <body>
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6" v-ref="title">
                The Perfect Landlord
            </p>
            <div class="redirection">
                <button id="tenant" @click="redirectTenant">I'm a Tenant</button>
                <button id="landlord" @click="redirectLandlord">I'm a Landlord</button>
            </div>
        </div>
    </section>

    </body>

    <div>
      <router-link to='/log-in' class="button is-dark mt-4 text-center">I am looking to rent my property</router-link>
    </div>

    <div>
      <router-link to='/log-in' class="button is-dark mt-4 text-center">I am looking to rent a property</router-link>
    </div>

>>>>>>> 6aaa6ea0310e6a63953ffb85987c4e174cdd3327
</template>

<script scoped>
    import HomePage from '../components/HomePage/HomePage.vue'
    import LoadingAnimated from '../components/LoadingAnimated.vue'

    export default{
        data(){
            return{
                loaded : true
            }
        },
        components:{
            LoadingAnimated,
            HomePage
        },
        methods:{

        },
        created(){
                setTimeout(()=> this.loaded = false, 2000)
        }
    }

</script>