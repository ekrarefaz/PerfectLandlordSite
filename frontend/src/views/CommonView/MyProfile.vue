<template>
    <div class='wrapper'>
        <div class='card' @click='detailsLoad'>
            <div class='cover-photo'>
                <img src='@/assets/logo.png' class='profile'>
            </div>
            <h3 class='profile-name'>{{ profile.user.username}}</h3>
            <p class='about'>{{ profile.user.groups[0].name}}</p>
            <div class='btnSection'>
                <button class='btn' @click='makeEditableForm' v-show='!editable'>Edit</button>
                <button class='btn' @click='saveUpdates' v-show='editable'>Save</button>
                <button class='btn' @click='logout'>Logout</button>
            </div>
        </div>

        <div class='card details' v-show='details'>
            <h3>Profile Details</h3>
            <div class='profile-info'>
                <p> Username: 
                    <span v-show='!editable' class='strong'>{{ profile.user.username}}</span>
                    <span v-show='editable'>
                        <input type='text' v-model='profile.user.username'>
                    </span>
                </p>
                <p> Date of Birth: 
                    <span v-show='!editable' class='strong'>{{ profile.birth_date}}</span>
                    <span v-show='editable'>
                        <input type='text' v-model='profile.birth_date'>
                    </span>
                </p>
                <p> About
                    <span v-show='!editable' class='strong'>{{profile.bio}}</span>
                    <span v-show='editable'>
                        <input type='text' v-model='profile.bio'>
                    </span>
                </p>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default{
    name: 'MyProfile',
    data(){
        return{
            details: false,
            editable: false,
            profile: {
                'user': {
                    'id': 1,
                    'username': '',
                    'email': '',
                    'groups': [
                        {
                            'name': ''
                        }
                    ],
                    'first_name': '',
                    'last_name': ''
                },
                'bio': '',
                'location': '',
                'birth_date': '',
                'get_image': '',
                'get_thumbnail': '',
                'get_full_name': ''
            }
        }
    },
    mounted(){
        this.getProfile()
        document.title = 'My Profile | The Perfect Landlord'
    },
    methods:{
        detailsLoad(){
            this.details = true
        },
        detailsHide(){
            if(this.editable == false){
                this.details = false
            }
        },
        makeEditableForm(){
            this.editable = true
            this.details = true
        },
        saveUpdates(){
            this.editable = false
        },
        logout(){
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getProfile() {
            const config = {'Authorization': 'Token 2765877aa300599722b10dee28051cfda41b815b'}

            await axios
                .get('v2/user/profile/', config)
                .then(response => {
                    console.log(response.data)
                    this.profile = response.data
                    console.log(this.profile)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async postUpdates(){
            const config = {'Authorization': 'Token 2765877aa300599722b10dee28051cfda41b815b'}
            const formData = {
                profile: this.profile
            }

            // POST CHANGED DATA
            await axios
            .post('v2/user/profile', formData)
            // Incomplete

        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700&display=swap');

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    color: black ;
}

body {
    background: #222;
    height: 100vh;
    display: grid;
    place-items: center;
    font-family: Montserrat;

}

.wrapper{
    display: flex;
}

.strong{
    font-size: 1.3em;
    color: maroon;
    font-style: bold;
}
.card {
    padding: 15px;
    width: 350px;
    background: whitesmoke;
    border: 2px solid maroon;
    border-radius: 5px;
    text-align: center;
    user-select: none;
    align-content: center;
}
.details{
    width: 70vw;
    border: none;
}

.profile-info{
    text-align: left;
    padding: 30px;

}

.cover-photo {
    position: relative;
    background: maroon ;
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
    background: transparent;
    border-color: maroon;
    color: maroon;
    width: 100px;
}

.btn:hover {
    background: maroon;
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
