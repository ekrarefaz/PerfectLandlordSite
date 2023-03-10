import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/CommonView/Home.vue';
import LandlordHome from '../views/LandlordView/LandlordHome.vue';
import Properties from '../views/TenantView/Properties.vue';
import Property from '../views/TenantView/Property.vue';
import SignUp from '../views/SignUp.vue';
import LogIn from '../views/CommonView/LogIn.vue';
import Tenants from '../views/LandlordView/Tenants.vue';
import About from '../views/CommonView/About.vue';
import UserProfile from '../views/CommonView/MyProfile.vue';
import LandlordProfile from '../views/LandlordView/LandlordProfile.vue';
import MyProperties from '../views/LandlordView/MyProperties.vue';
import TenantInspection from '@/views/TenantView/TenantInspection.vue';
import SavedProperties from '@/views/TenantView/SavedProperties.vue';
import TenantApplications from '@/views/TenantView/TenantApplications.vue';
import LandlordApplications from '@/views/LandlordView/LandlordApplications.vue';
import ApplicationForm from '@/views/CommonView/ApplicationForm.vue';
import PropertyDetails from '@/views/LandlordView/PropertyDetails.vue';
import LandlordInspections from '@/views/LandlordView/LandlordInspections.vue';
import LandlordLogin from '@/views/LandlordView/LandlordLogin.vue';
import TenantLogin from '@/views/TenantView/TenantLogin.vue';
import LandlordSignup from '@/views/LandlordView/LandlordSignup.vue';
import TenantSignup from '@/views/TenantView/TenantSignup.vue'; 
import TenantDetails from '@/views/LandlordView/TenantDetails.vue'; 


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/landlord',
    name: 'landlord',
    component: LandlordHome,
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: SignUp,
  },
  {
    path: '/tenant-login',
    name: 'tenant-login',
    component: TenantLogin,
  },
  {
    path: '/landlord-login',
    name: 'landlord-login',
    component: LandlordLogin,
  },
  {
    path: '/tenant-signup',
    name: 'tenant-signup',
    component: TenantSignup,
  },
  {
    path: '/landlord-signup',
    name: 'landlord-signup',
    component: LandlordSignup,
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
    path: '/properties/:property_slug',
    name: 'Property',
    component: Property,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/properties/:property_slug/inspection', // Slug Used Inspection Tab
    name: 'tenant-inspections',
    component: TenantInspection,
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
    props: true
  },
  {
    path: '/tenant/:name',
    // path: '/tenant-details',
    name: 'tenant-details',
    component: TenantDetails,
    // meta:{
    //   requiredLogin:true
    // }
    props: true
  },
  {
    path: '/tenant-profile',
    name: 'profile',
    component: UserProfile,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/landlord-profile',
    name: 'landlordprofile',
    component: UserProfile,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/landlord-properties',
    name: 'landlord-properties',
    component: MyProperties,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/landlord-inspections',
    name: 'landlord-inspections',
    component: LandlordInspections,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/landlord-applications',
    name: 'landlord-applications',
    component: LandlordApplications,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/landlord-properties/:property_slug',
    name: 'property-details',
    component: PropertyDetails,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/saved-properties',
    name: 'saved-properties',
    component: SavedProperties,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/properties/:property_slug/applications',
    name: 'tenant-applications',
    component: TenantApplications,
    // meta:{
    //   requiredLogin:true
    // }
  },
  {
    path: '/application-form',
    name: 'application-form',
    component: ApplicationForm,
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
