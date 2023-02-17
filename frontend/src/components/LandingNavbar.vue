<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item"><strong>The Perfect Landlord</strong></router-link>
  
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
  
        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
          <div class="navbar-end">
            <router-link to="/properties" class="navbar-item">Properties</router-link>
            <router-link to="/tenants" class="navbar-item">Tenants</router-link>

            <div class="navbar-item">
              <div class="buttons">                 
                <router-link to="/log-in" class="button is-light">Log in</router-link>
                <router-link to="/profile" class="button is-success">
                  <span class="icon"><i class="fas fa-user"></i></span>
                  <span>Profile</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
</template>
<script>
    export default{
        data() {
            return {
                showMobileMenu: false,
        }
  },
}
</script>