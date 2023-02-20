from django.urls import include, path
from rest_framework import routers

from . import views

# CRUD API
router = routers.DefaultRouter()

# router.register(r'users', views.UserList)
# router.register(r'groups', views.GroupList)
# router.register(r'properties', views.PropertiesList)

urlpatterns = [
    # App API
    # path('profile/', views.ProfileView.as_view()),
    # path('my-properties/', views.PropertiesListRestricted.as_view()),
    # path('my-properties/search/', views.search),
    # path('properties/filter/', views.filter),
    # path('my-properties/<slug:property_slug>', views.PropertyDetails.as_view()),
    # path('tenants/', views.TenantProfilesList.as_view()),
]

urlpatterns += router.urls