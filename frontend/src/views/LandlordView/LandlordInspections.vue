<template>
        <LandlordSubNav/>
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
                    <i class="fa fa-pen" @click="makeEditableForm" v-show="!editable"></i>
                    <i class="fa fa-print" @click="saveUpdates" v-show="editable"></i>
                    
                </div>

                <div class="datetime">
                    <p> Date: 
                        <span v-show="!editable" class="strong">{{inspectionDate}}</span>
                        <span v-show="editable">
                            <input type="text" v-model="inspectionDate">
                        </span>
                    </p>
                </div>
                <div class="datetime">
                <p> Time: 
                    <span v-show="!editable" class="strong">{{inspectionTime}}</span>
                    <span v-show="editable">
                        <input type="text" v-model="inspectionTime">
                    </span>
                </p>
                </div>
            </div>
        </div>
</template>
    
    
<style>
    .property-address{
        text-align: center;
    }
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


<script>
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';
import InspectionCard from '@/components/Tenant/InspectionCard.vue';

    export default{
        data(){
            return{
                editable: false,
                inspectionDate: "11/11/23",
                inspectionTime: "13:15"
            }
        },
        components: { InspectionCard, LandlordSubNav },
        methods:{
            makeEditableForm(){
                this.editable = true
            },
            saveUpdates(){
                this.editable = false
            }
        }
}
</script>