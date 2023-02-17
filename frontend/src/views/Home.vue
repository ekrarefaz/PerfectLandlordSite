<template>
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

</template>
<script>
    export default{
        data(){
            return{
                title: "The Perfect Landlord",
                index: 0
            }
        },
        methods:{
            redirectTenant(){
                this.$router.push('/tenant-home')
            },
            redirectLandlord(){
                this.$router.push('/landlord-home')
            },
            writeText(){
                this.$refs["title"] = text.slice(0,this.index);
                this.index++;
            }
        },
        mounted(){
            this.writeText
        }
}
</script>
<style scoped>
    button{
        padding:1rem;
        border-radius: 5px;
        border:none;
    }
    .redirection{
        margin: 10px;
        padding: 10px;
    }
</style>