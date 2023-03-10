<template>

                <div class="overlay" v-if="showModal" @click="showModal = false"></div>

                <div class="modal" v-if="showModal">
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
                                <button class="button is-dark">Register</button>
                            </div>
                        </div>
                        <hr>
                    </form>
                </div>
            </div>
            </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default{
        data(){
            return{
                showModal: false,
            }
        },
        components:{

        },
        methods:{

        },
        mounted(){

        }
    }
</script>

<style scoped>

</style>