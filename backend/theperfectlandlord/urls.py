from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication API
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    # App API
    path('api/landlord/', include('landlord.urls')),
    path('api/agent/', include('agent.urls')),
    path('api/tenant/', include('tenant.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

