<template>
    <h2>Tenants Looking to Rent</h2>
    <button id="filterBtn" @click="showFilter">Filter</button>
    <div v-if="filterVisible">
        <TenantFilter/>
    </div>
    <div v-if="tenants">
        <div class="tenant-container">
            <div v-for="tenant in tenants" :key="tenant.id">
                <router-link to="/">
                <div class="tenant">
                    <div class="image">
                        <img src="../assets/logo.png" alt="">
                    </div>
                    <div class="details">
                        <h3>{{tenant.name}} ({{tenant.age}})</h3>
                        <sub>{{tenant.gender}}</sub>
                        <br>
                        <p>{{tenant.job}}</p>
                        <p>Preference: {{tenant.preference.type}}</p>
                    </div>
                </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import TenantFilter from '../components/Filters/TenantFilter.vue';
    export default{
    data() {
        return {
            tenants: [],
            filterVisible: false
        };
    },
    methods: {
        showFilter() {
            this.filterVisible = !this.filterVisible;
        }
    },

    mounted() {
        this.getMyProperties()
        document.title = 'Tenants | The Perfect Landlord'
    },
    methods: {
        showFilter(){
                this.filterVisible = !this.filterVisible
        },
        async getMyProperties() {
        const config = {'Authorization': 'Token 01ff9afdd60b6d23b92b5eed55dd87831a30bc9c'}

        await axios
            .get('/tenants/', config)
            .then(response => {
            console.log(response.data[0])
            this.tenants = response.data
            })
            .catch(error => {
            console.log(error)
            })
        }
    },
    components: {
    
        TenantFilter
    }
}
</script>

<style scoped>

*{
    text-decoration: none;
}
.tenant-container{
    display: flex;
    align-content: space-around;
    padding: 10px;
    width:max-content;
    height: max-content;
    text-decoration: none;
    flex: 0 0 192px;
}
.tenant{
    text-decoration: none;
    border: 2px solid black;
    padding: 20px;
    margin: 15px;
    display: flex;
    align-content: space-between;

}
.tenant:hover{
    background:whitesmoke;
    border-radius: 10px;
    font-size: 1.05em;
}
.tenant a{
    text-decoration: none;
    color: black;
}
.image,.details{
    padding: 5px;
    text-decoration: none;
}
img{
    width: 100px;
    height: 100px;
}


</style>