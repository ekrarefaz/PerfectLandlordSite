<template>
    <TenantSubNav/>
    <div class="inspection-container"> 
        <div>
            <div class="property-address">
                <h1>8/3 Kooyongkoot Road</h1>             
            </div>
            <div class="datetime">
                <div class="date">
                    <strong>Date: {{date}}</strong>
                </div>
                <div class="time">
                    <strong>Time: {{time}}</strong>
                </div>
                <div class="register">
                    <i class="fas fa-user-plus" @click="registerInspection">Register</i>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import TenantSubNav from '@/components/Tenant/TenantSubNav.vue';

    export default{
    data() {
        return {
            inspections: null,
            time: "13:45",
            date: "11/11/23",
        };
    },
    methods: {
        registerInspection() {
            // REGISTER INSPECTION 
        }
    },
    components: { TenantSubNav }
}
</script>

<style>
.inspection-container{
    border: solid 2px maroon;
    margin: 20px;
    padding: 20px;
}
.datetime{
    background-color: beige;
    padding: 20px;
    display: flex;
    justify-content: space-around;
}
.date,.time, .register{
    margin: 5px;
    padding: 10px;
}

</style>