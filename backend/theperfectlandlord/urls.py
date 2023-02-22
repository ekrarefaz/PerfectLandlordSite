from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),

    # Authentication API
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    # App API
    path('api/landlord/', include('landlord.urls')),
    path('api/agent/', include('agent.urls')),
    path('api/tenant/', include('tenant.urls')),

    # App API v2
    path('api/v2/property/', include('property.urls')),
    path('api/v2/user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

