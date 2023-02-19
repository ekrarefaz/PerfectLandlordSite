<template>
<<<<<<< HEAD
  <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;700;900&display=swap" rel="stylesheet">
<nav>
  <div class="box-shadow">
    <div class="section logo">
      <span class="white">ThePerfect</span><span class="green">Landlord</span>
    </div>
    <div class="section">
      <ul>
        <li><router-link to="/" class="active">Home</router-link></li>
          <li><router-link to="/log-in">Login</router-link></li>
          <li><router-link to="/sign-up">Signup</router-link></li>
          <li><router-link to="/profile">Profile</router-link></li>

      </ul>
    </div>
  </div>
</nav>
=======
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
>>>>>>> 6aaa6ea0310e6a63953ffb85987c4e174cdd3327
</template>
<style>
:root {
  --gray: grey;
  --black: #000;
  --white: #fff;
  --green: gold;
  --body-background: #fff;
  --hover-color: grey;
  --header-background: #000;
  --anchor-color: #fff;
  --heading-color: #b2b2b2;
  --paragraph-color: #b2b2b2;
  --anchor-active-color: gold;
}  

nav{
  width: 100vw;
  margin: 0;
}
.green {
  color: var(--green);
}

.white {
  color: var(--white);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}


a {
  text-decoration: none;
}

a.active {
  color: var(--anchor-active-color);
  font-weight: var(--anchor-active-font-weight);
}

a:hover {
  color: var(--hover-color);
}

.box-shadow {
  display: flex;
  background-color: var(--header-background);
  padding-top: 5px;
  justify-content: space-around;
  flex-flow: row wrap;
}

.section {
  flex-grow: 1;
}

.section.logo {
  margin-left: 2.5em;
}

.logo {
  font-size: 1.2em;
  font-weight: bold;
  text-transform: uppercase;
}

ul {
  list-style-type: none;
  display: flex;
  flex-flow: row nowrap;
  width: 500px;
  margin: 0;
  padding: 0;
}

ul li {
  flex-grow: 1;
  text-align: center;
  width: 70px;
}

ul li a {
  color: var(--anchor-color);
  font-size: .9rem;
  text-transform: uppercase;
}

.box-shadow div:nth-child(1) {
  flex-grow: 8;
  padding-bottom: 15px;
}

header div:nth-child(1) img {
  margin-left: 25px;
}

.box-shadow {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  background-color: #000;
}

@media all and (max-width: 800px) {
  header {
      justify-content: space-around;
  }

  .container {
      padding: 50px;
  }
}

@media only screen and (max-width:542px) {
  header div:nth-child(1) {
      margin: 0 auto;
      display: block;
      padding-bottom: 0;
  }

  header {
      flex-direction: column;
  }

  .section {
      flex-grow: 1;
      text-align: center;
  }

  .section.logo {
      margin: 0;
  }

  ul {
      background-color: #232323;
      width: 100%;
      margin-top: 15px;
  }

  ul li {
      width: 50%;
      padding: 5px;
  }
}
</style>