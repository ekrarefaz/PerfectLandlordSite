<template>
    <form id="job-form">
      <label>Personal Information</label>
        <section class="personal-info-wrapper">
          <div class="row">
            <div class="col-4">
              <label class="form-label">First Name</label>
              <input v-model="firstname" id="first-name" type="text" required />
            </div>
            <div class="col-4">
              <label class="form-label">Last Name</label>
              <input v-model="lastname" type="text" required />
            </div>
          </div>
          <div class="row">
            <div class="col-7">
              <label class="form-label">Email</label>
              <input v-model="email" type="email" required />
            </div>
          </div>
          <div class="row">
            <div class="col-9">
              <label class="form-label">Street Address</label>
              <input v-model="address1" type="text" placeholder="Address Line 1" />
            </div>
          </div>
          <div class="row">
            <div class="col-9">
              <input v-model="address2" type="text" placeholder="Address Line 2" />
            </div>
          </div>
          <div class="row">
            <div class="col-4">
              <input v-model="city" type="text" placeholder="City" />
            </div>
            <div class="col-4">
              <input v-model="state" type="text" placeholder="State" />
            </div>
            <div class="col-4">
              <input v-model="zipcode" type="text" placeholder="Zip Code" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
              <label class="form-label">Mobile Phone</label>
              <input v-model="phone" type="text" />
            </div>
          </div>
        </section>
      
      <label>Rental Profile</label>
        <section class="renter-profile-wrapper">
          <section class="form-field-section">
            <label>Current or Most Recent</label>
          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Agent/Landlord</label>
                <input v-model="agent" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input v-model="prevAddress1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input v-model="prevAddress2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input v-model="prevCity" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input v-model="prevState" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input v-model="prevZip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Phone</label>
                <input v-model="prevAgentPhone" type="text" />
              </div>
            </div>

          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Start Date</label>
                <input v-model="prevStartDate" type="date" />
              </div>
              <div class="col-3">
                <label class="form-label">End Date</label>
                <input v-model="prevEndDate" type="date" />
              </div>
              <div class="col-3">
                <label>Proof of Residence</label>
                <input type="file" ref="file">
                <button @click="submitResidenceProof"></button>
              </div>
            </div>
          </section>

          <section class="form-field-section">
            <div class="row">
              <div class="col-12">
                <label class="form-label">Reason for Leaving</label>
                <input v-model="prevLeaveReason" type="text" />
              </div>
            </div>
          </section>
          </section>
          <label>Employment History</label>
          <section class="employment-history-wrapper">
          <section class="form-field-section">
            <label>Current Employment</label>
          </section>
      
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Employer</label>
                <input v-model="employer" type="text" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input v-model="empAddress1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input v-model="empAddress2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input v-model="empcity" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input v-model="empstate" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input v-model="empzip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Phone</label>
                <input v-model="empphone" type="text" />
              </div>
            </div>
    
          </section>
          <section class="form-field-section">
            <div class="row">
              <div class="col-3">
                <label class="form-label">Income</label>
                <input type="number"/>
              </div>
            </div>
          </section>
      
          <section class="form-field-section">
            <div class="row">
              <div class="col-5">
                <label class="form-label">Frequency</label>
                <select>
                  <option value="weekly">Weekly</option>
                  <option value="fortnightly">Fortnightly</option>
                  <option value="monthly">Monthly</option>
                </select>
              </div>
              <div class="col-3">
                <label>Payslips (3 recent)</label>
                <input type="file" ref="file">
                <button @click="submitIncomeProof"></button>
              </div>
            </div>
          </section>
        </section>
      
        <label>Personal References</label>
        <section class="reference-wrapper">
          <section class="form-field-section">
            <h4 class="form-section-title">Reference 1</h4>
            <div class="row">
              <div class="col-6">
                <label class="form-label">Name</label>
                <input v-model="refname" type="text" />
              </div>
              <div class="col-6">
                <label class="form-label">Phone</label>
                <input v-model="ref1phone" type="text" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input v-model="ref1address1" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input v-model="ref1address2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input v-model="ref1city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input v-model="ref1state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input v-model="ref1zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section>
      
          <!-- <section class="form-field-section">
            <h4 class="form-section-title">Reference 2</h4>
            <div class="row">
              <div class="col-6">
                <label class="form-label">Name</label>
                <input v-model="ref2name" type="text" />
              </div>
              <div class="col-6">
                <label class="form-label">Phone</label>
                <input v-model="ref2phone" type="text" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <label class="form-label">Address</label>
                <input v-model="ref1address2" type="text" placeholder="Address Line 1" />
              </div>
            </div>
            <div class="row">
              <div class="col-9">
                <input v-model="ref1address2" type="text" placeholder="Address Line 2" />
              </div>
            </div>
            <div class="row">
              <div class="col-4">
                <input v-model="ref2city" type="text" placeholder="City" />
              </div>
              <div class="col-4">
                <input v-model="ref2state" type="text" placeholder="State" />
              </div>
              <div class="col-4">
                <input v-model="ref2zip" type="text" placeholder="Zip Code" />
              </div>
            </div>
          </section> -->
        </section>
        <input type="submit" value="Submit" />
      </form>
</template>
<script>
  import axios from 'axios'

  export default{
    data(){
      return{
        payslip: null,
        identification: null,

        // Personal
        firstname: "",
        lastname: "",
        email:"",
        address1: "",
        address2: "",
        city: "",
        state: "",
        zip: "",
        phone: "",
        //Residential
        agent: "",
        prevAddress1: "",
        prevAddress2: "",
        prevCity: "",
        prevState: "",
        prevZip:"",
        prevAgentPhone:"",
        prevStartDate:"",
        prevEndDate:"",
        prevLeaveReason:"",
        //Employment
        employer: "",
        empAddress1: "",
        empAddress2:"",
        empcity:"",
        empstate:"",
        empzip:"",
        empphone:"",
        //Reference
        refname:"",
        ref1phone:"",
        ref1address1:"",
        ref1address2:"",
        ref1city:"",
        ref1state:"",
        ref1zip:""
      }
    },
    methods:{
      submitIncomeProof() {
        const formData = new FormData();
        formData.append('file', this.Images);
        const headers = { 'Content-Type': 'multipart/form-data' };
        axios.post('v2/application/income/add', formData, { headers }).then((res) => {
          res.data.files; // binary representation of the file
          res.status; // HTTP status
        });
      },
      submitResidenceProof() {
        const formData = new FormData();
        formData.append('file', this.Images);
        const headers = { 'Content-Type': 'multipart/form-data' };
        axios.post('v2/application/residential/add', formData, { headers }).then((res) => {
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
  .personal-info-wrapper{
    border: 2px solid grey;
    border-radius: 5px;
    width: 100%;
    margin: 10px;
    padding: 10px;
  }
  .renter-profile-wrapper{
    border: 2px solid grey;
    border-radius: 5px;
    width: 100%;
    margin: 10px;
    padding: 10px;
  }
  .employment-history-wrapper{
    border: 2px solid grey;
    border-radius: 5px;
    width: 100%;
    margin: 10px;
    padding: 10px;
  }
  .reference-wrapper{
    border: 2px solid grey;
    border-radius: 5px;
    width: 100%;
    margin: 10px;
    padding: 10px;
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