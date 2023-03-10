<template>
  <div class="tenant-container">
    <div class="card" v-for="tenant in tenants">
        <div class="cover-photo">
            <img src="@/assets/logo.png" class="profile">
        </div>
        <h3 class="profile-name">{{tenant.get_full_name}}</h3>
        <p class="about">{{tenant.user.groups[0].name}}</p>
        <router-link :to="{name: 'tenant-details', params:{name: tenant.get_full_name}}">
          <button class="btn">Details</button>
        </router-link>
    </div>
</div>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700&display=swap");

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  color: black ;
}

.tenant-container{
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
.card {
  padding: 15px;
  width: 350px;
  background: whitesmoke;

  border-radius: 5px;
  text-align: center;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.7);
  user-select: none;
  align-content: center;
  margin: 30px;
}

.cover-photo {
  position: relative;
  background: url(https://i.imgur.com/jxyuizJ.jpeg);
  background-size: cover;
  height: 180px;
  border-radius: 5px 5px 0 0;
}

.profile {
  position: absolute;
  width: 120px;
  bottom: -60px;
  left: 15px;
  border-radius: 50%;
  border: 2px solid #222;
  background: #222;
  padding: 5px;
}

.profile-name {
  font-size: 20px;
  margin: 25px 0 0 120px;
}

.about {
  margin-top: 30px;
  line-height: 1.6;
}

.btn {
  margin: 30px 15px;
  background: #7ce3ff;
  padding: 10px 25px;
  border-radius: 3px;
  border: 1px solid #7ce3ff;
  font-weight: bold;
  font-family: Montserrat;
  cursor: pointer;
  color: #222;
  transition: 0.2s;
}

.btn:last-of-type {
  background: transparent;
  border-color: #7ce3ff;
  color: #7ce3ff;
}

.btn:hover {
  background: #7ce3ff;
  color: #222;
}

.icons {
  width: 180px;
  margin: 0 auto 10px;
  display: flex;
  justify-content: space-between;
  gap: 15px;
}

.icons i {
  cursor: pointer;
  padding: 5px;
  font-size: 18px;
  transition: 0.2s;
}

.icons i:hover {
  color: #7ce3ff;
}

</style>


<script>
import axios from 'axios'

import LoggedInNavbar from '@/components/LoggedInNavbar.vue'
import UserProfile from '@/components/UserProfile.vue';
import LandlordNav from '@/components/Landlord/LandlordNav.vue';
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';

export default {
  name: 'Tenants',
  data() {
    return {
      tenants: [],
      filterVisible: false,
    }
  },
  components: {
    LoggedInNavbar,
    UserProfile,
    LandlordNav,
    LandlordSubNav
},
  mounted() {
    this.getTenants()
    document.title = 'Tenant | The Perfect Landlord'
    localStorage.setItem("pageType", "landlord")
  },
  methods: {
    showFilter() {
          this.filterVisible = !this.filterVisible;
    },
    async getTenants() {
      const config = {'Authorization': `Token ${localStorage.getItem("token")}`}  

      await axios
        .get('v2/user/tenants', config)
        .then(response => {
          console.log(response.data)
          this.tenants = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

