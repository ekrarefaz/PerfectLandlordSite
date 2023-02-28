from django.urls import include, path
from rest_framework import routers

from . import views

# CRUD API
router = routers.DefaultRouter()

# router.register(r'users', views.UserList)

urlpatterns = [    
    path('signup/', views.Signup.as_view()),
    path('profile/', views.MyProfile.as_view()),
    path('tenants/', views.Tenants.as_view())
]

urlpatterns += router.urls