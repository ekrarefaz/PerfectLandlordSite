from django.urls import include, path
from rest_framework import routers

from . import views

# CRUD API
router = routers.DefaultRouter()

# router.register(r'groups', views.GroupList)
# router.register(r'properties', views.PropertiesList)

urlpatterns = [
    path('properties/', views.PropertiesList.as_view()),
    path('properties/search/', views.search),
    path('properties/filter/', views.filter),
    path('properties/saved/', views.SavedPropertiesList.as_view()),
    # path('my-properties/<slug:property_slug>', views.PropertyDetails.as_view()),
    # path('tenants/', views.TenantProfilesList.as_view()),
]

urlpatterns += router.urls