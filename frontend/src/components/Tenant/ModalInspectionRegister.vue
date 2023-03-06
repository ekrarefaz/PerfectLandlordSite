<template>
    <div class="popup">
        <div class="innerpop">
            <slot/>
        </div>
    </div>
</template> 

<style>
    .popup{
        color: white;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 99;
        background-color: rgba(0, 0, 0, 0);

        display: flex;
        align-items: center;
        justify-content: center;
    }
    .innerpop{
        background-color: black;;
        padding: 30px;
        width: 60%;
        color: white;
    }
</style>

<script>
    export default{

    }
</script>