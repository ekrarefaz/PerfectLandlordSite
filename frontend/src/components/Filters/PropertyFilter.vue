<template>
    <form>  
        <div class="form-content">
            <h1>Property Type</h1>
            <div class="form-section-1">
                <input type="checkbox" value="House">
                <label> House </label>
                <label> Apartment/Flat</label>
                <input type="checkbox" value="Town House">
                <label> Town House</label>
                <input type="checkbox" value="Studio">
                <label>Studio</label>
                <input type="checkbox" value="Retirement Home">
                <label>Retirement Home</label>
            </div>
            <div class="form-section-2">
                <h4>Property Details</h4>
                <label>Parking</label>
                <select>
                    <option value="On-Site">onsite</option>
                    <option value="On-Street">on-street</option>
                    <option value="None">None</option>
                </select>
                <div class="room">
                    <label>Rooms</label>
                    <input type="number" name="minroom" >
                </div>
                <div class="toilet">
                    <label>Bathrooms</label>
                    <input type="number" name="minbath" >
                </div>
                <select>
                    <option value="Full">Fully Furnished</option>
                    <option value="Semi">Semi Furnished</option>
                    <option value="None">Not Furnished</option>
                </select>
                <h4>Property Features</h4>
                <input type="checkbox" value="Heating">
                <label> Heating</label>
                <input type="checkbox" value="AirCon">
                <label> AirCon</label>
                <input type="checkbox" value="Laundry">
                <label>Laundry</label>
                <input type="checkbox" value="Gym">
                <label>Gym</label>
                <input type="checkbox" value="Pool">
                <label>Pool</label>
            </div>
        </div>
        <button>
            <i class="fas fa-filter" @click="filterProperties">Filter Properties</i>
        </button>
        
        </form>
</template>
<style scoped>
    form {
        max-width: 700px;
        margin: 10px auto;
        padding: 10px 20px;
        background: #f4f7f8;
        border-radius: 8px;
        z-index: 2;
    }
    input,
    select{
        background: rgba(255, 255, 255, 0.1);
        border: none;
        font-size: 16px;
        height: auto;
        margin: 0;
        outline: 0;
        padding: 15px;
        width: 50%;
        background-color: #e8eeef;
        color: #8a97a0;
        box-shadow: 0 1px 0 rgba(0, 0, 0, 0.03) inset;
        margin-bottom: 30px;
    }
    input[type="radio"],
    input[type="checkbox"] {
        margin: 0 4px 8px 0;
    }

    button {
        padding: 19px 39px 18px 39px;
        color: black;
        font-size: 10px;
        text-align: center;
        font-style: normal;
        border-radius: 5px;
        width: 30%;
        box-shadow: 0 -1px 0 rgba(255, 255, 255, 0.1) inset;
        margin-bottom: 10px;
        margin-left: 200px;
    }
      
    select {
    padding: 6px;
    height: 32px;
    border-radius: 2px;
    }
    
    label {
        display: block;
        margin-bottom: 8px;
    }

    .form-content{
        padding: 5px;
        margin: 20px;
    }
    .form-section-1{
        margin: 0px;
        align-content: left;
        padding: 25px;
    }
    .form-section-2{
        margin: 10px;
        align-content: left;
        padding: 10px;
    }
    form input{
        padding: 5px;
        margin: 20px;
    }
    form select{
        padding: 5px;
        margin: 20px;
    }
    .form-section-3{
        margin: 10px;
        align-content: left;
        padding: 10px;

    }
</style>
<script>
    export default{
        methods:{
            filterProperties(){
                // Connect filter backend
            }
        }
    }
</script>