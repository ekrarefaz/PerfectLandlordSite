<template>
    <form>  
        <div class="form-content">
            <div class="form-section-1">
                <h4>Tenant Type</h4>
                <input type="checkbox" value="Student">
                <label> Student</label>
                <input type="checkbox" value="Single Professional">
                <label> Single Professional</label>
                <input type="checkbox" value="Senior Citizen">
                <label> Senior Citizen</label>
                <input type="checkbox" value="Couple">
                <label> Couple</label>
                <input type="checkbox" value="Special Needs">
                <label> Special Needs</label>
            </div>
            <div class="form-section-2">
                <h4>Tenant Details</h4>
                <label>Gender</label>
                <select>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="pefer not to say">Prefer not to say</option>
                </select>
                
                <label>Religion</label>
                <select>
                    <option value="Catholic">Catholic</option>
                    <option value="Muslim">Muslim</option>
                    <option value="Hindu">Hindu</option>
                    <option value="Buddhist">Buddhist</option>
                </select>
                <div class="ageInput">
                    <label>Age Range</label>
                    <input type="number" name="minAge" > -
                    <input type="number" name="maxAge">
                </div>
            </div>
            <div class="form-section-3">
                <h4>Tenant Hobbies</h4>
                <input type="checkbox" value="Music">
                <label> Music</label>
                <input type="checkbox" value="Gardening">
                <label> Gardening</label>
                <input type="checkbox" value="Cooking">
                <label> Cooking</label>
                <input type="checkbox" value="Sports">
                <label> Sports</label>
                <input type="text" value="Other">
                <label>Other</label>
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
    }
    .form-section-2{
        border: 2px solid black;
        margin: 10px;
        align-content: left;
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
    }
</style>