from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('compras/', include('apps.compras.urls')),
    path('saidas/', include('apps.saidas.urls')),
    path('pecas/', include('apps.pecas.urls')),
    path('unidades/', include('apps.unidades.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)