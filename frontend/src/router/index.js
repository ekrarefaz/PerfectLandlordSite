import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/CommonView/Home.vue';
import Properties from '../views/TenantView/Properties.vue';
import Property from '../views/TenantView/Property.vue';
import SignUp from '../views/SignUp.vue';
import LogIn from '../views/CommonView/LogIn.vue';
import Tenants from '../views/LandlordView/Tenants.vue';
import About from '../views/CommonView/About.vue';
import UserProfile from '../views/TenantView/UserProfile.vue';
import LandlordProfile from '../views/LandlordView/LandlordProfile.vue';
import InspectionCard from '../components/Tenant/InspectionCard.vue';

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
    path: '/:property_slug/inspections',
    name: 'inspections',
    component: InspectionCard,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/tenants',
    name: 'tenants',
    component: Tenants,
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
  {
    path: '/landlord-profile',
    name: 'landlordprofile',
    component: LandlordProfile,
    // meta:{
    //   requiredLogin:true
    // }
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiredLogin) &&
    !store.state.isAuthenticated
  ) {
    next('/login');
  } else {
    next();
  }
});

export default router;
