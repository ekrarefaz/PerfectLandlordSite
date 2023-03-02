<template>
    <div class="inspection-container">
        <!-- DATABASEREAD -->
        <!-- <div v-for="inspection in inspections" :key="inspection.id">
        <div class="property-address">
            <h1>{{inspection.address}}</h1>
        </div>
        <div class="datetime">
            <div class="date">
                <strong>{{inspection.date}}</strong>
            </div>
            <div class="time">
                <strong>{{inspection.time}}</strong>
            </div>
        </div>
        </div> -->

        <!-- HARDCODED -->
        <div>
            <div class="property-address">
                <h1>8/3 Kooyongkoot Road</h1>
            </div>
            <div class="datetime">
                <div class="date">
                    <strong>11/11/23</strong>
                </div>
                <div class="time">
                    <strong>13:15</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                inspections: null
            }
        },
        // mounted(){
        //     fetch('http://localhost:3000/inspections')
        //     .then(res => res.json())
        //     .then(data => this.inspections = data)
        //     .catch(err => console.log(err.message))
        // }
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
    align-content: space-between;
}
.date,.time{
    margin: 5px;
    padding: 10px;
}

</style>