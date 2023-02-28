from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),

    # Authentication API
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    # App API v2
    path('api/v2/property/', include('property.urls')),
    path('api/v2/user/', include('user.urls')),
    path('api/v2/inspection/', include('inspection.urls')),
    path('api/v2/application/', include('application.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)