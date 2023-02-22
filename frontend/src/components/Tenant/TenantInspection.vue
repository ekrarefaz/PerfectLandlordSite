
<template>
    <TenantSubNav/>
    <InspectionCard/>
</template>

<script>
    import InspectionCard from './InspectionCard.vue';
    import TenantSubNav from '../../components/Tenant/TenantSubNav.vue'
    export default{
        components:{
            InspectionCard,
            TenantSubNav
        }
    }
</script>