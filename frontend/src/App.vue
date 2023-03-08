<template>
  <div v-if="userRole == ''">
    <LandingNavbar/>
  </div>
  <div v-else-if="userRole == 'Landlord'">
    <LandlordNav/>
  </div>
  <div v-else-if="userRole == 'Tenant'">
    <TenantNav/>
  </div>
  <body>
    <div id="wrapper">
      <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
        <div class="lds-dual-ring"></div>
      </div>

      <section class="section">
        <router-view/>
      </section>
    </div>
  </body>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2023</p>
  </footer>


</template>

<script>
import axios from 'axios'
import LandingNavbar from './components/LandingNavbar.vue';
import LandlordNav from './components/Landlord/LandlordNav.vue';
import TenantNav from './components/Tenant/TenantNav.vue';

export default {
    data() {
        return {
          userRole: localStorage.getItem("role")
        };
    },
    components: { LandingNavbar, LandlordNav, TenantNav },
    beforeCreate() {
        this.$store.commit("initialize");
        const token = this.$store.state.token;
        if (token) {
            axios.defaults.headers.common["Authorization"] = "Token " + token;
        }
        else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
    methods:{
      getUserRole(){
        this.userRole = localStorage.getItem("role")
      }
    }
}
</script>

<style lang="scss">

@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

</style>
