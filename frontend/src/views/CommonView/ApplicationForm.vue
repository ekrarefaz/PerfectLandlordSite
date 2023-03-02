<template>
    <form id="job-form">
        <section>
          <h2 class="form-section-title">Personal Information</h2>
          <div class="row">
            <div class="col-4">
              <label class="form-label">First Name</label>
              <input name="first-name" id="first-name" type="text" required />
            </div>
            <div class="col-4">
              <label class="form-label">Last Name</label>
              <input name="last-name" type="text" required />
            </div>
          </div>
          <div class="row">
            <div class="col-7">
              <label class="form-label">Email</label>
              <input name="email" type="email" required />
            </div>
          </div>
          <div class="row">
            <div class="col-9">
              <label class="form-label">Street Address</label>
              <input name="address-1" type="text" placeholder="Address Line 1" />
            </div>
          </div>
          <div class="row">
            <div class="col-9">
              <input name="address-2" type="text" placeholder="Address Line 2" />
            </div>
          </div>
          <div class="row">
            <div class="col-4">
              <input name="city" type="text" placeholder="City" />
            </div>
            <div class="col-4">
              <input name="state" type="text" placeholder="State" />
            </div>
            <div class="col-4">
              <input name="zipcode" type="text" placeholder="Zip Code" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
              <label class="form-label">Home Phone</label>
              <input name="home-phone" type="text" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
              <label class="form-label">Mobile Phone</label>
              <input name="mobile-phone" type="text" />
            </div>
          </div>
          
          <div class="row">
            <div class="col-3">
              <label class="form-label">Are you 18 or older?</label>
              <input name="older-than-18" type="radio" value="yes" required /><span class="radio-selection"> Yes</span> <input name="older-than-18" type="radio" value="no" /><span class="radio-selection"> No</span>
            </div>
            <div class="col-3">
              <label class="form-label">If yes, Date of Birth</label>
              <input name="date-of-birth" type="date" />
            </div>
          </div>
      
          <div class="row">
            <div class="col-6">
              <label class="form-label">Have you been convicted of a misdemeanor or felony, or been incarcerated in connection with a felony, in the past seven years?</label>
              <input name="convicted" type="radio" value="yes" required /><span class="radio-selection"> Yes</span> <input name="convicted" type="radio" value="no" /><span class="radio-selection"> No</span>
            </div>
          </div>
          <div class="row">
            <div class="col-12">
              <label class="form-label">If yes, please explain:</label>
              <input name="convicted-reason" type="text" />
            </div>
          </div>
        </section>
      
      
        <section>
          <h2 class="form-section-title">Prior Tenancy</h2>
          <section class="form-field-section">
            <h3 class="form-section-title">Current or Most Recent</h3>
          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Agent/Landlord</label>
                <input name="emp1-employer" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input name="emp1-address-1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input name="emp1-address-2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input name="emp1-city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input name="emp1-state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input name="emp1-zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Phone</label>
                <input name="emp1-phone" type="text" />
              </div>
            </div>
      
            <div class="row">
              <div class="col-5">
                <label class="form-label">Name of Immediate Contact</label>
                <input name="emp1-supervisor" type="text" />
              </div>
            </div>
          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Start Date</label>
                <input name="emp1-start-date" type="date" />
              </div>
              <div class="col-3">
                <label class="form-label">End Date</label>
                <input name="emp1-end-date" type="date" />
              </div>
            </div>
          </section>

          <section class="form-field-section">
            <div class="row">
              <div class="col-12">
                <label class="form-label">Reason for Leaving</label>
                <input name="emp1-reason-for-leaving" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <h3 class="form-section-title">Cuurent Employment</h3>
          </section>
      
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Employer</label>
                <input name="emp2-employer" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input name="emp2-address-1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input name="emp2-address-2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input name="emp2-city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input name="emp2-state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input name="emp2-zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Phone</label>
                <input name="emp2-phone" type="text" />
              </div>
            </div>
      
            <div class="row">
              <div class="col-5">
                <label class="form-label">Name of Immediate Supervisor</label>
                <input name="emp2-supervisor" type="text" />
              </div>
            </div>
          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Start Date</label>
                <input name="emp2-start-date" type="date" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-5">
                <label class="form-label">Position/Job Title</label>
                <input name="emp2-title" type="text" />
              </div>
              <div class="col-3">
                <label>Payslips</label>
                <input type="file" ref="file">
                <button @click="submitFile">Upload Payslips</button>
              </div>
            </div>
          </section>

          <section class="form-field-section">
            <h3 class="form-section-title">Prior Employment</h3>
          </section>
      
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Employer</label>
                <input name="emp3-employer" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input name="emp3-address-1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input name="emp3-address-2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input name="emp3-city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input name="emp3-state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input name="emp3-zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Phone</label>
                <input name="emp3-phone" type="text" />
              </div>
            </div>
      
            <div class="row">
              <div class="col-5">
                <label class="form-label">Name of Immediate Supervisor</label>
                <input name="emp3-supervisor" type="text" />
              </div>
            </div>
          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Start Date</label>
                <input name="emp3-start-date" type="date" />
              </div>
              <div class="col-3">
                <label class="form-label">End Date</label>
                <input name="emp3-end-date" type="date" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-5">
                <label class="form-label">Position/Job Title</label>
                <input name="emp3-title" type="text" />
              </div>
              <div class="col-3">
                <label class="form-label">Payrate</label>
                <input name="emp3-payrate" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-12">
                <label class="form-label">Reason for Leaving</label>
                <input name="emp3-reason-for-leaving" type="text" />
              </div>
              <div class="col-12">
                <label class="form-label">May We Contact?</label>
                <input name="emp3-can-contact" type="radio" value="yes" /><span class="radio-selection"> Yes</span> <input name="emp3-can-contact" type="radio" value="no" /><span class="radio-selection"> No</span>
              </div>
            </div>
          </section>
        </section>
      
        <section>
          <h2 class="form-section-title">Personal References</h2>
          <section class="form-field-section">
            <h4 class="form-section-title">Reference 1</h4>
            <div class="row">
              <div class="col-6">
                <label class="form-label">Name</label>
                <input name="ref1-name" type="text" />
              </div>
              <div class="col-6">
                <label class="form-label">Phone</label>
                <input name="ref1-phone" type="text" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input name="ref1-address-1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input name="ref1-address-2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input name="ref1-city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input name="ref1-state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input name="ref1-zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <h4 class="form-section-title">Reference 2</h4>
            <div class="row">
              <div class="col-6">
                <label class="form-label">Name</label>
                <input name="ref2-name" type="text" />
              </div>
              <div class="col-6">
                <label class="form-label">Phone</label>
                <input name="ref2-phone" type="text" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input name="ref2-address-1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input name="ref2-address-2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input name="ref2-city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input name="ref2-state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input name="ref2-zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
        </section>
        <input type="submit" value="Submit" />
      </form>
</template>
<script>
  export default{
    data(){
      return{
        payslip: null,
        identification: null,
      }
    },
    methods:{
      submitFile() {
        const formData = new FormData();
        formData.append('file', this.Images);
        const headers = { 'Content-Type': 'multipart/form-data' };
        axios.post('http://127.0.0.1/api/v2/application/submit', formData, { headers }).then((res) => {
          res.data.files; // binary representation of the file
          res.status; // HTTP status
        });
      },
    }
  }
</script>
<style scoped>
form {
    max-width: 900px;
    margin: auto;
  }
  
  body {
    padding: 20px 20px;
  }
  
  h2.form-title,
  h2.form-section-title {
    font-family: 'Open Sans Condensed', Helvetica, sans-serif;
    font-size: 1.5rem;
    color: #000;
    line-height: 1.15rem;
    margin: 50px;
  }
  
  h3.form-section-title {
    font-family: 'Open Sans Condensed', Helvetica, sans-serif;
    font-size: 1.25rem;
    color: #000;
    line-height: 1.2rem;
  }
  
  h4.form-section-title {
    font-family: 'Open Sans Condensed', Helvetica, sans-serif;
    font-size: 1.0rem;
    color: #000;
    line-height: 0.95rem;
  }
  
  .form-label {
    display: block;
    font-family: 'Open Sans Condensed', Helvetica, sans-serif;
    font-size: 0.875rem;
    color: #000;
    font-weight: 700;
    line-height: 100%;
  }
  
  .form-field-section {
    margin: 10px 0;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="date"] {
    width: 100%;
  }
  
  .radio-selection {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.8125rem;
    color: #000;
  }
  
  * {
    box-sizing: border-box;
  }
  
  .col-1 {
    width: 8.33%;
  }
  
  .col-2 {
    width: 16.66%;
  }
  
  .col-3 {
    width: 25%;
  }
  
  .col-4 {
    width: 33.33%;
  }
  
  .col-5 {
    width: 41.66%;
  }
  
  .col-6 {
    width: 50%;
  }
  
  .col-7 {
    width: 58.33%;
  }
  
  .col-8 {
    width: 66.66%;
  }
  
  .col-9 {
    width: 75%;
  }
  
  .col-10 {
    width: 83.33%;
  }
  
  .col-11 {
    width: 91.66%;
  }
  
  .col-12 {
    width: 100%;
  }
  
  [class*="col-"] {
    float: left;
    padding: 15px;
  }
  
  .row::after {
    content: "";
    clear: both;
    display: block;
  }
</style>