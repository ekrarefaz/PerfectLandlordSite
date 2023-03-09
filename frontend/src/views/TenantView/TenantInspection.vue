<template>
    <TenantSubNav/>
    <div class="inspection-container"> 
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
                <div>
                    <i class="fas fa-plus" @click="showModal = true">Register</i>
                </div>
            </div>
        </div>
            <ModalInspectionRegister v-if="showModal">
                <div class="page-sign-up">
                    <div class="columns">
                        <div class="column is-4 is-offset-4">
                            <h1 class="title">Inspection Registration</h1>
                            <form @submit.prevent="submitForm">
                                <div class="field">
                                    <label>Email</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="email">
                                    </div>
                                </div>
            
                                <div class="field">
                                    <label>First Name</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="fname">
                                    </div>
                                </div>
            
                                <div class="field">
                                    <label>Phone</label>
                                    <div class="control">
                                        <input type="number" class="input" v-model="phone">
                                    </div>
                                </div>
            
                                <div class="field">
                                    <div class="control">
                                        <button class="button is-dark" @click="registerInspection">Register</button>                                        
                                        <button class="button is-dark" @click="showModal=false">Cancel</button>
                                    </div>
                                </div>
                                <hr>
                            </form>
                        </div>
                    </div>
                </div>
            </ModalInspectionRegister>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import TenantSubNav from '@/components/Tenant/TenantSubNav.vue';
import RegisterInspection from '@/components/Tenant/RegisterInspection.vue';
import ModalInspectionRegister from '@/components/Modals/ModalInspectionRegister.vue';

    export default{
    data() {
        return {
            email: "",
            fname: "",
            phone: "",
            inspections: null,
            time: "",
            date: "",

            showModal: false,
        };
    },

    mounted(){
        this.getInspections()
    },

    methods: {

        modalToggle(){
            this.showModal = true
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
        registerInspection() {
                const formData = {
                    email: this.email,
                    fname: this.fname,
                    phone: this.phone
                }
                axios
                    .post("v2/inspection/register/", formData)
                    .then(response => {
                        toast({
                            message: 'Registered',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('./')
                    })
            }
        },
    components: {
        TenantSubNav,
        RegisterInspection,
        ModalInspectionRegister
    },
}
</script>

<style scoped>

.title{
    color: white;
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
    justify-content: space-around;
}
.date,.time, .register{
    margin: 5px;
    padding: 10px;
}

</style>