from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # <-- AÑADE ESTA LÍNEA

urlpatterns = [
    # AÑADE ESTA NUEVA RUTA:
    # Redirige la página principal (/) a /ordenes/
    path('', RedirectView.as_view(url='/ordenes/', permanent=True)),

    path('admin/', admin.site.urls),
    path('ordenes/', include('ordenes.urls')),
]
