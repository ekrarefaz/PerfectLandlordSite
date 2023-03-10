<template>
        <LandlordSubNav/>
        <div class="inspection-container">
            <div v-for="inspection in inspections"></div>
            <div class="inspection1">
                <div class="property-address">
                    <h1>8/3 Kooyongkoot Road</h1>
                    <div class="icon-section">
                        <div class="icon-sub-section1">
                            <i class="fa fa-pen" @click="makeEditableForm" v-show="!editable"> Edit</i>
                            <i class="fa fa-print" @click="saveUpdates" v-show="editable"> Save</i>
                        </div>
                        <div class="icon-sub-section2">
                            <i class="fa fa-plus" @click="showModal=true"> Add Inspection</i>
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
            <ModalInspectionCreate v-show="showModal">
                <div class="page-sign-up">
                    <div class="columns">
                        <div class="column is-4 is-offset-4">
                            <h1 class="title">Add Inspection</h1>
                            <form @submit.prevent="submitForm">
                                <div class="field">
                                    <label>Address</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="newAddress">
                                    </div>
                                </div>
            
                                <div class="field">
                                    <label>Date</label>
                                    <div class="control">
                                        <input type="date" class="input" v-model="newdate">
                                    </div>
                                </div>
            
                                <div class="field">
                                    <label>Time</label>
                                    <div class="control">
                                        <input type="time" class="input" v-model="newTime">
                                    </div>
                                </div>
            
                                <div class="field">
                                    <div class="control">
                                        <button class="button is-dark" @click="addInspection">Add</button>                                        
                                        <button class="button is-dark" @click="showModal=false">Cancel</button>
                                    </div>
                                </div>
                                <hr>
                            </form>
                        </div>
                    </div>
                </div>
            </ModalInspectionCreate>
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
import axios from 'axios'
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';
import ModalInspectionCreate from '@/components/Modals/ModalInspectionCreate.vue';
import InspectionCard from '@/components/Tenant/InspectionCard.vue';

    export default{
        data(){
            return{
                showModal: false,

                inspections: [],
                newInspection: false,
                editable: false,

                newAddress: "",
                newdate: "",
                newTime: "",

                //dummy
                inspectionDate: ["11/11/23",""],
                inspectionTime: ["13:35", ""]

            }
        },
        mounted(){
            this.getInspections()
        },
        components: { InspectionCard, LandlordSubNav, ModalInspectionCreate },
        methods:{
            makeEditableForm(){
                this.editable = true
            },
            saveUpdates(){
                this.editable = false
            },
            async getInspections() {
            const config = {'Authorization': `Token ${localStorage.getItem("token")}`}  

            await axios
                .get('v2/inspection/view/', config)
                .then(response => {
                console.log(response.data)
                this.inspections = response.data
                console.log(this.inspections)
                })
                .catch(error => {
                console.log(error)
                })
            },
            addInspection(){
                const formData = {
                    address: this.address,
                    date: this.date,
                    time: this.time
                }

                axios
                    .post("v2/inspection/create/", formData)
                    .then(response => {
                        toast({
                            message: 'Inspection Added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                    })
            }
        }
}
</script>