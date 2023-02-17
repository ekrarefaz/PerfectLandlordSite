from django.urls import include, path
from rest_framework import routers

from . import views

# CRUD API
router = routers.DefaultRouter()

router.register(r'users', views.UserList)
router.register(r'groups', views.GroupList)

urlpatterns = [
    # Authentication API
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # App API
    path('profile/', views.ProfileView.as_view()),
    path('properties/', views.PropertiesListRestricted.as_view()),
    path('properties/<slug:property_slug>', views.PropertyDetails.as_view()),
    path('tenants/', views.TenantProfilesList.as_view()),
]