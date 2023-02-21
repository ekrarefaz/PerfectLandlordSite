<template>
    <Navbar/>
    <h1>Hello this is home for landlord. Please navigate around</h1>

</template>

<script>
    import Navbar from '@/components/Landlord/LandlordNav.vue'

    export default{
        data(){
            return{
                loaded : true
            }
        },
        components:{
            Navbar
        },
        methods:{

        },
        created(){
                setTimeout(()=> this.loaded = false, 2000)
        }
    }

</script>