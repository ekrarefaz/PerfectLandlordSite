<template>
    <body>
        <section class="row-1">
            <section class="nav-section">
            </section>
            <section class="text-section">
            <section class="section-absolute">
                <h1 id="title-slide">Discover your perfect abode</h1>
                <p id="text-slide">
                    At The PerfectLandlord, we are committed to making the rental process as seamless and stress-free as possible.
                    Whether you're a seasoned renter or a first-time tenant, we provide the support and guidance you need to find your perfect abode.
                </p>
                <router-link to="/about">
                Explore
                <svg width="40" height="12" xmlns="http://www.w3.org/2000/svg"><path d="M34.05 0l5.481 5.527h.008v.008L40 6l-.461.465v.063l-.062-.001L34.049 12l-.662-.668 4.765-4.805H0v-1h38.206l-4.82-4.86L34.05 0z" fill="#000" fill-rule="nonzero"/></svg>
                </router-link>
            </section>
            </section>
        </section>
    
      <!-- ROW 2 -->
      <section class="row-2">
        <div id="img1"></div>
        <section>
          <h2>What are we about?</h2>
          <p>
            Welcome to The PerfectLandlord, the innovative platform that connects landlords with tenants directly, without the need for intermediaries or middlemen. 
            Our goal is to revolutionize the rental market in Australia by providing a fast, secure, and reliable service that simplifies the rental process for both landlords and tenants.
          </p>
        </section>
        <div id="img2"></div>
      </section>
    </body>
</template>
<script>
    export default{ 
        metaInfo: {
            script: [
                { src: './home.js', async: true, defer: true }
            ],
        },
        data(){
            return{
                title: "The Perfect Landlord",
                loaded: true,
                index: 0
            }
        },
        components:{
            
        },
        methods:{
            redirectTenant(){
                this.$router.push('/tenant-home')
            },
            redirectLandlord(){
                this.$router.push('/landlord-home')
            },
            writeText(){
                this.$refs["title"] = text.slice(0,this.index);
                this.index++;
            }
        },
        mounted(){
            this.writeText
        },
}
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Spartan:wght@500;600;700&display=swap");

:root {
  --darkGray: hsl(0, 0%, 63%);
  --veryDarkGray: hsl(0, 0%, 27%);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Spartan", sans-serif;
}
body{
    padding-top: 50px;
}
.row-1 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70vh;
  width: 100%;
}

.nav-section {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  width: 70%;
  height: 100%;
  background-image: url('../../assets/chris-robert--ryDtcapIas-unsplash.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: left center;
  animation-duration: 15s;
  animation-timing-function: cubic-bezier(0.445, 0.05, 0.55, 0.95);
  animation-iteration-count: infinite;
  transition: all cubic-bezier(0.165, 0.84, 0.44, 1) 1s;
}

@keyframes moveBackground {
  0% {
    background-position: left bottom;
    background-size: cover 70vh;
    transition: all cubic-bezier(0.075, 0.82, 0.165, 1) 2s;
  }
  25% {
    background-position: center center;
    background-size: cover 73vh;
    transition: all cubic-bezier(0.075, 0.82, 0.165, 1) 2s;
  }
  50% {
    background-position: right top;
    background-size: cover 75vh;
    transition: all cubic-bezier(0.075, 0.82, 0.165, 1) 2s;
  }
  75% {
    background-position: center center;
    background-size: cover 73vh;
    transition: all cubic-bezier(0.075, 0.82, 0.165, 1) 2s;
  }
  100% {
    background-position: left bottom;
    background-size: cover 70vh;
    transition: all cubic-bezier(0.075, 0.82, 0.165, 1) 2s;
  }
}

.nav-section nav {
  margin-top: 30px;
  margin-left: 30px;
  z-index: 2;
}

.nav-section nav button {
  display: none;
}

.nav-section nav a {
  color: #fff;
  margin: 0 15px;
  font-size: 14px;
  text-decoration: none;
  cursor: pointer;
  padding: 5px 0;
  border-bottom: 2px solid transparent;
}

.nav-section nav a:nth-child(2) {
  border: none;
}

.nav-section nav a:hover {
  border-bottom-color: #fff;
  transition: all cubic-bezier(0.165, 0.84, 0.44, 1) 1s;
}

.text-section {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 30%;
  height: 100%;
  background-color: #fff;
}

.text-section .section-absolute {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-direction: column;
  position: absolute;
  padding: 0 50px;
  height: 70vh;
  width: 30%;
}

.text-section .section-absolute h1 {
  font-size: 2em;
  font-weight: 700;
}

.text-section .section-absolute p {
  font-size: 12px;
  color: var(--veryDarkGray);
  margin: 20px 0;
  line-height: 22px;
}

.text-section .section-absolute a {
  text-decoration: none;
  color: #000;
  text-transform: uppercase;
  letter-spacing: 10px;
  margin-bottom: 50px;
}

.text-section .section-absolute a:hover {
  color: var(--darkGray);
  transition: all cubic-bezier(0.165, 0.84, 0.44, 1) 1s;
}

.text-section .section-absolute .controllers-section {
  position: absolute;
  left: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-self: center;
  width: 30%;
  background-color: #000;
}

.text-section .section-absolute .controllers-section button {
  background-color: #000;
  border: none;
  width: 50%;
  padding: 10px 0;
  cursor: pointer;
  outline: none;
}

.text-section .section-absolute .controllers-section button:hover {
  background-color: var(--veryDarkGray);
  transition: all cubic-bezier(0.165, 0.84, 0.44, 1) 1s;
}

.row-2 {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 30vh;
  background-color: #fff;
}



.row-2 section {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-direction: column;
  width: 58%;
  padding: 0 30px;
  height: 30vh;
}

.row-2 section h2 {
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 10px;
  font-size: 1em;
}

.row-2 section p {
  font-size: 12px;
  color: var(--veryDarkGray);
  margin-top: 20px;
  line-height: 22px;
}

@media (max-width: 1200px) {
  .nav-section {
    width: 60%;
  }
  .text-section {
    width: 40%;
  }
  .text-section .section-absolute {
    width: 40%;
  }
  .text-section .section-absolute .controllers-section {
    width: 20%;
  }
  .row-2 #img1 {
    width: 32%;
  }
  .row-2 #img2 {
    width: 32%;
  }
  .row-2 section {
    width: 36%;
    padding: 20px;
  }
  .row-2 section h2 {
    font-size: 0.8em;
  }
  .row-2 section p {
    font-size: 0.6em;
    line-height: 16px;
  }
}

@media (max-width: 990px) {
  .row-1,
  .row-2 {
    flex-direction: column;
    height: auto;
  }
  .nav-section {
    height: 50vh;
    width: 100%;
  }
  .nav-section nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 30px 20px;
    margin: 0;
  }
  .nav-section nav button {
    display: block;
    cursor: pointer;
  }
  .nav-section nav a {
    display: none;
    margin: 0 5px;
    font-weight: 600;
    color: black;
  }
  .nav-section nav a:nth-child(2) {
    padding: 0;
    margin: 0;
    display: block;
  }
  .nav-section nav button {
    background-color: transparent;
    border: none;
    outline: none;
  }
  .text-section {
    height: auto;
    width: 100%;
  }
  .text-section .section-absolute {
    position: relative;
    width: 100%;
    height: auto;
    padding: 30px 20px;
  }
  .text-section .section-absolute h1 {
    font-size: 1.5em;
  }
  .text-section .section-absolute p {
    margin: 30px 0;
    font-size: 0.8em;
    line-height: 28px;
  }
  .text-section .section-absolute .controllers-section {
    top: -50px;
    height: 50px;
    left: unset;
    right: 0;
  }
  .row-2 #img1,
  .row-2 #img2 {
    width: 100%;
    height: 30vh;
  }
  .row-2 section {
    height: auto;
    width: 100%;
    padding: 30px 20px;
  }
  .row-2 section h2 {
    font-size: 0.9em;
    letter-spacing: 5px;
  }
  .row-2 section p {
    font-size: 0.8em;
    line-height: 28px;
  }
}
.attribution {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      font-size: 11px;
      text-align: center;
      background-color: #000;
      padding: 8px;
      color: #fff;
    }

    .attribution span {
      margin: 5px 0;
    }

    .attribution a {
      color: #fff;
      font-weight: 700;
    }
</style>