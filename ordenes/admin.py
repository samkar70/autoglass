from django.contrib import admin
from .models import Orden

# Esto registra tu modelo Orden en el panel de admin
admin.site.register(Orden)
