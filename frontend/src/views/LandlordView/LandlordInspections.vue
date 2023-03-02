<template>
        <LandlordSubNav/>
        <div class="inspection-container">
            <div class="inspection1">
                <div class="property-address">
                    <h1>8/3 Kooyongkoot Road</h1>
                    <div class="icon-section">
                        <div class="icon-sub-section1">
                            <i class="fa fa-pen" @click="makeEditableForm" v-show="!editable"> Edit</i>
                            <i class="fa fa-print" @click="saveUpdates" v-show="editable"> Save</i>
                        </div>
                        <div class="icon-sub-section2">
                            <i class="fa fa-plus" @click="addInspection"> Add Inspection Time</i>
                        </div>
                    </div>
                </div>

                <div class="datetime">
                    <p> Date: 
                        <span v-show="!editable" class="strong">{{inspectionDate[0]}}</span>
                        <span v-show="editable">
                            <input type="text" v-model="inspectionDate[0]">
                        </span>
                    </p>
                </div>
                <div class="datetime">
                <p> Time: 
                    <span v-show="!editable" class="strong">{{inspectionTime[0]}}</span>
                    <span v-show="editable">
                        <input type="text" v-model="inspectionTime[0]">
                    </span>
                </p>
                </div>
            </div>
            <div class="inspection2" v-show="newInspection">
                <div class="property-address">
                    <h1>8/3 Kooyongkoot Road</h1>
                    <div class="icon-section">
                        <div class="icon-sub-section1">
                            <i class="fa fa-pen" @click="makeEditableForm" v-show="!editable"> Edit</i>
                            <i class="fa fa-print" @click="saveUpdates" v-show="editable"> Save</i>
                        </div>
                        <div class="icon-sub-section2">
                            <i class="fa fa-plus">Add Inspection Time</i>
                        </div>
                    </div>
                </div>

                <div class="datetime">
                    <p> Date: 
                        <span v-show="!editable" class="strong">{{inspectionDate[1]}}</span>
                        <span v-show="editable">
                            <input type="text" v-model="inspectionDate[1]">
                        </span>
                    </p>
                </div>
                <div class="datetime">
                <p> Time: 
                    <span v-show="!editable" class="strong">{{inspectionTime[1]}}</span>
                    <span v-show="editable">
                        <input type="text" v-model="inspectionTime[1]">
                    </span>
                </p>
                </div>
            </div>
        </div>
</template>
    
    
<style>
    i:hover{
        cursor: pointer;
    }
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
                newInspection: false,
                editable: false,
                inspectionDate: ["11/11/23",""],
                inspectionTime: ["13:35", ""]

            }
        },
        components: { InspectionCard, LandlordSubNav },
        methods:{
            makeEditableForm(){
                this.editable = true
            },
            saveUpdates(){
                this.editable = false
            },
            addInspection(){
                this.newInspection = true
            }
        }
}
</script>