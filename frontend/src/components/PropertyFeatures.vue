<template>
    <div class="features">
        <div class="indoors">
            <ul>
                <div v-for="feature in features"><li>{{features}}</li></div>
            </ul>
        </div>
        <div class="outdoors">
            <ul>
                <li>outdoors</li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default{
        data(){
            return{

            }
        },
        props: ['features'],

    }
</script>

<style> 

</style>