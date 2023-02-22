<template>
    <div v-show="loaded">
        <LoadingAnimated/>
    </div>
    <div v-show="!loaded">
        <HomePage/>
    </div>
</template>

<script scoped>
    import HomePage from '@/components/HomePage/HomePage.vue'
    import LoadingAnimated from '@/components/LoadingAnimated.vue'

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
        },
        mounted(){
            localStorage.setItem("pageType", "common")
        }
    }

</script>