from django.urls import include, path
from rest_framework import routers

from . import views

urlpatterns = [
    # App API
    path('submit/', views.SubmitApplication.as_view()),
    path('identity/list/', views.IdentityList.as_view()),
    path('identity/add/', views.AddIdentity.as_view()),
    path('residential/list/', views.ResidentialList.as_view()),
    path('residential/add/', views.AddResidential.as_view()),
    path('employment/list/', views.EmploymentList.as_view()),
    path('employment/add/', views.AddEmployment.as_view()),
    path('income/list/', views.IncomeList.as_view()),
    path('income/add/', views.AddIncome.as_view()),
]