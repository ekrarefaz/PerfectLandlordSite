<template>
    <h1>Hello this is home for landlord. Please navigate around</h1>

</template>

<script>
    import LandlordNav from '@/components/Landlord/LandlordNav.vue'

    export default{
        data(){
            return{
                loaded : true
            }
        },
        components:{
            LandlordNav
        },
        methods:{

        },
        created(){
                setTimeout(()=> this.loaded = false, 2000)
        },
        mounted(){
            localStorage.setItem("pageType", "landlord")
        }
    }

</script>