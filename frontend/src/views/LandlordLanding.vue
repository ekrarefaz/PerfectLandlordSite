<template>
    <body>
        <button @click="goTenants">Looking for your best tenant</button>
    </body>
</template>

<style scoped>
*{
    box-sizing: border-box;
}
body{
    display: flex;
    align-items:center;
    justify-content: center;
    margin:0;
    min-height: 100vh;
    color: cornsilk;
    font-size: 2rem;
}
button{
    padding:3rem;
    border-radius: 5px;
    border:2px solid black;
}
</style>

<script>
    export default{
        data(){
            return{

            }
        },
        methods:{
            goTenants(){
                this.$router.push("/tenants")
            }
        }
    }
</script>