<template>
    <div class="subnav">
        <LoginSubnav/>
    </div>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Landlord Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username" name="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password" name="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log in</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/landlord-signup">click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .page-log-in{
        margin: 30px;
    }
</style>
<script>
import LoginSubnav from '@/components/Common/LoginSubnav.vue'
import axios from 'axios'

export default {
    name: "LogIn",
    data() {
        return {
            username: "",
            password: "",
            errors: [],
            profile: {},
        };
    },
    mounted() {
        document.title = "Log In";
    },
    methods: {        
        async submitForm() {
            // Reset authorization and token
            axios.defaults.headers.common["Authorization"] = "";
            localStorage.removeItem("token");
            var token = '';

            // Retrieve username and password from user
            const formData = {
                username: this.username,
                password: this.password
            };

            await axios
                .post("auth/token/login/", formData)
                .then(response => {
                    token = response.data.auth_token;
                })
                .catch(error => {
                    this.errors.push('Your username / password is invalid')    
                    console.log(JSON.stringify(error))
                });

            // Get user profile using token
            if (token != '') {
                await axios
                    .get('v2/user/profile/', { 
                        // Set temporary axios header
                        "headers": {
                            'Authorization': `Token ${token}`   
                        }
                    })
                    .then(response => {                
                        this.profile = response.data;

                        // Check if user is landlord
                        if (this.profile.user.groups.find(e=> e.name == 'Landlord')) {

                            // Save token in store/index
                            this.$store.commit("setToken", token);

                            // Set token as authorization default header
                            axios.defaults.headers.common["Authorization"] = "Token " + token;

                            // Set local storage so user would still be logged in even after refresh
                            localStorage.setItem("token", token);
                            localStorage.setItem("user", this.username);

                            // Set role in local storage
                            localStorage.setItem("role", 'Landlord')                            

                            // Route to landlord page
                            const toPath = this.$route.query.to || "/tenants";                                                                      
                            this.$router.push(toPath);                              
                        }
                        else {
                            this.errors.push('You are not authorized as a landlord') 
                        }
                    })
                    .catch(error => {
                        this.errors.push('Something went wrong')
                        console.log(JSON.stringify(error))
                    })           
            }        
        }
    },
    components: { LoginSubnav }
}
</script>