import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/CommonView/Home.vue';
import LandlordHome from '../views/LandlordView/LandlordHome.vue';
import Properties from '../views/TenantView/Properties.vue';
import Property from '../views/TenantView/Property.vue';
import SignUp from '../views/SignUp.vue';
import LogIn from '../views/CommonView/LogIn.vue';
import Tenants from '../views/LandlordView/Tenants.vue';
import About from '../views/CommonView/About.vue';
import TenantProfile from '../views/TenantView/TenantProfile.vue';
import LandlordProfile from '../views/LandlordView/LandlordProfile.vue';
import MyProperties from '../views/LandlordView/MyProperties.vue';
import TenantInspection from '@/components/Tenant/TenantInspection.vue';
import SavedProperties from '@/views/TenantView/SavedProperties.vue';
import TenantApplications from '@/views/TenantView/TenantApplications.vue';
import ApplicationForm from '@/views/CommonView/ApplicationForm.vue';
import PropertyDetails from '@/views/LandlordView/PropertyDetails.vue';
import LandlordInspections from '@/views/LandlordView/LandlordInspections.vue';

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
    // path: '/:property_slug/inspections', // Slug Used Inspection Tab
    path: '/tenant-inspections', // Hardcoded
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
  },
  {
    path: '/tenant-profile',
    name: 'profile',
    component: TenantProfile,
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
    path: '/property-details',
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
    path: '/tenant-applications',
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
