import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Properties from '../views/Properties.vue';
import Property from '../views/PropertyDetails.vue';
import SignUp from '../views/SignUp.vue';
import LogIn from '../views/LogIn.vue';
import About from '../views/About.vue';
import UserProfile from '../views/UserProfile.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: SignUp,
  },
  {
    path: '/log-in',
    name: 'login',
    component: LogIn,
  },
  {
    path: '/about',
    name: 'about',
    component: About,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/properties',
    name: 'properties',
    component: Properties,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/:property_slug',
    name: 'property-details',
    component: Property,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfile,
    // meta:{
    //   requiredLogin:true
    // }
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to,from,next) => {
  if(to.matched.some(record=>record.meta.requiredLogin) && !store.state.isAuthenticated){
    next('/login')
  }
  else{
    next()
  }
})

export default router;
