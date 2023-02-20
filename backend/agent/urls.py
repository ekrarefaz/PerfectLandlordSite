from django.urls import include, path
from rest_framework import routers

from . import views

# CRUD API
router = routers.DefaultRouter()

router.register(r'inspections', views.InspectionsList)

urlpatterns = [
    path('<slug:property_slug>/inspections/', views.PropertyInspectionList.as_view()),
] 

urlpatterns += router.urls