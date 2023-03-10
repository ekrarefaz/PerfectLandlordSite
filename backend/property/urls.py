from django.urls import include, path
from rest_framework import routers

from . import views

# CRUD API
router = routers.DefaultRouter()

# router.register(r'users', views.UserList)

urlpatterns = [
    # App API
    path('properties/', views.Properties.as_view()),
    path('properties/<slug:property_slug>/', views.PropertyDetails.as_view()),
    path('my-properties/', views.MyProperties.as_view()),
    path('saved-properties/', views.SavedProperties.as_view()),
    path('search/', views.SearchProperties.as_view()),
    path('filter/', views.FilterProperties.as_view()),
]

urlpatterns += router.urls