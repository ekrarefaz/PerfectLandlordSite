<template>
    <div v-if="pageType == 'common'">
        <LandingNavbar/>
      </div>
      <div v-else-if="pageType == 'landlord'">
        <LandlordNav/>
      </div>
      <div v-else-if="pageType == 'tenant'">
        <TenantNav/>
      </div>
</template>
<script>
    import LandingNavbar from '@/components/LandingNavbar.vue';
    import LandlordNav from '@/components/Landlord/LandlordNav.vue';
    import TenantNav from '@/components/Tenant/TenantNav.vue';
    export default{
    methods:{
        getPageType(){
        this.pageType = localStorage.getItem("pageType")
      }
    },
    components:{
        LandingNavbar,
        LandlordNav,
        TenantNav
    },
    data() {
        return {
          pageType: 'common'
        };
    },
    beforeMount(){
        this.getPageType()
    }
    }
</script>

