<template>
    <form>  
        <div class="form-content">
            <div class="form-section-1">
                <h4>House Type</h4>
                <input type="checkbox" value="House">
                <label> House</label>
                <input type="checkbox" value="Apartment">
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
                <label>Religion</label>
                <select>
                    <option value="Catholic">Catholic</option>
                    <option value="Muslim">Muslim</option>
                    <option value="Hindu">Hindu</option>
                    <option value="Buddhist">Buddhist</option>
                </select>
                <div class="room">
                    <label>Rooms</label>
                    <input type="number" name="minroom" > -
                    <input type="number" name="maxroom">
                </div>
                <div class="toilet">
                    <label>Bathrooms</label>
                    <input type="number" name="minbath" > -
                    <input type="number" name="maxbath">
                </div>
                <select>
                    <option value="Full">Fully Furnished</option>
                    <option value="Semi">Semi Furnished</option>
                    <option value="None">Not Furnished</option>
                </select>
            </div>
            <div class="form-section-3">
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
        <button type="submit"> Submit </button>
    </form>
</template>
<style>
    .form-content{
        border: 1px solid black;
        padding: 5px;
        margin: 20px;
    }
    .form-section-1{
        border: 2px solid black;
        margin: 10px;
        align-content: left;
        padding: 10px;
    }
    .form-section-2{
        border: 2px solid black;
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
        border: 2px solid black;
        margin: 10px;
        align-content: left;
        padding: 10px;

    }
</style>