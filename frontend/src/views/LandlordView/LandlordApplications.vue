<template>
    <LandlordSubNav/>
    <div class="container">
        <div class="card card1" @click="showDetails">
                <div class="flex-section1">
                    <div class="applicantImg">
                        <img src="@/assets/jeff.jpg">
                    </div>
                </div>
                <div class="flex-section2">
                    <div class="applicantInfo">
                        <div class="info-top">
                            <div class="titleName">
                                <h3 class="applicantName">
                                    {{ applicantName[0] }}
                                </h3>
                            </div>
                            <div class="rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                            </div>
                        </div>
                    </div>
                    <div class="info-bottom">
                        <p><strong>Offered </strong>500$/week</p>
                        <p><strong>Application Date </strong>11/11/23</p>
                        <p>I am interested in this property because I live nearby and would be easy for me to shift</p>
                    </div>
                </div>
                <Details>
                <div class="expand-info">
                    <label>Income</label>
                    <div class="income-details">
                        <p><strong>Source </strong>Part-Time Job</p>
                        <p><strong>Weekly Income </strong>$700</p>
                        <p><strong>Income Proof </strong><i class="fas fa-file"> Files</i></p>
                    </div>
                    <label>Residential History</label>
                    <p><strong>Address </strong>22/3 Launder Street</p>
                    <p><strong>Monthly Rent </strong>$715</p>
                    <p><strong>Reference Contact </strong>0404786756</p>
                    <p><strong>Tenant History Proof </strong><i class="fa fa-file">Files </i></p>
                </div>
                </Details>
        </div>
        <div class="card card2">
            <div class="flex-section1">
                <div class="applicantImg">
                    <img src="@/assets/zuck.jpg">
                </div>
            </div>
            <div class="flex-section2">
                <div class="applicantInfo">
                    <div class="info-top">
                        <div class="titleName">
                            <h3 class="applicantName">
                                {{ applicantName[1] }}
                            </h3>
                        </div>
                        <div class="rating">
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                        </div>
                    </div>
                </div>
                <div class="info-bottom">
                    <p><strong>Offered </strong>500$/week</p>
                    <p><strong>Application Date </strong>11/11/23</p>
                    <p>I am interested in this property because I live nearby and would be easy for me to shift</p>
                </div>
            </div>
            <Details>
            <div class="expand-info">
                <label>Income</label>
                <div class="income-details">
                    <p><strong>Source </strong>Part-Time Job</p>
                    <p><strong>Weekly Income </strong>$700</p>
                    <p><strong>Income Proof </strong><i class="fas fa-file"> Files</i></p>
                </div>
                <label>Residential History</label>
                <p><strong>Address </strong>22/3 Launder Street</p>
                <p><strong>Monthly Rent </strong>$715</p>
                <p><strong>Reference Contact </strong>0404786756</p>
                <p><strong>Tenant History Proof </strong><i class="fa fa-file">Files </i></p>
            </div>
            </Details>
        </div>
    </div>
</template>

<style scoped>
    .container{
        margin-top: 10px;
    }
    .flex-section{
        display: flex;
        justify-content: space-evenly;
    }
    .card{
        background-color: whitesmoke;
        border: 1px solid maroon;
        padding: 20px;
    }
    .applicantImg{
        width: 150px;
        height: 150px;
        margin: 5px;
    }
    img{
        width: 100%;
        height: 100%;
    }
    .info-top{
        display: flex;
        justify-content: flex-start;
    }
    .titleName{
        padding-bottom: 20px;
    }
    .expand-info{
        margin-top: 50px;
        padding: 10px;
        margin-left: 50px;
    }

</style>

<script>
import LandlordSubNav from '@/components/Landlord/LandlordSubNav.vue';

    export default{
        data(){
            return{
                detailedView: false,
                applicantName: ["Jeff Mezos", "Elon Busk"]
            }
        },
        components: { LandlordSubNav },
        methods:{
            showDetails(){
                this.detailedView = !this.detailedView
            }
        }
}
</script>