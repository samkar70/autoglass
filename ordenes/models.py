from django.db import models
from django.utils import timezone

class Orden(models.Model):
    # --- Información del Cliente y Vehículo (sin cambios) ---
    cliente_nombre = models.CharField(max_length=200)
    cliente_telefono = models.CharField(max_length=20, blank=True)
    vehiculo = models.CharField(max_length=200, help_text="Ej: Toyota Camry 2022")

    # --- Detalles del Trabajo (sin cambios) ---
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADO', 'Completado'),
    ]
    descripcion_servicio = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    
    # --- Fecha de Creación (sin cambios) ---
    fecha_creacion = models.DateTimeField(default=timezone.now)

    # --- NUEVOS CAMPOS PARA GPS Y MILLAJE ---
    latitud_inicio = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_inicio = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitud_fin = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud_fin = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    millaje_recorrido = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Orden #{self.id} para {self.cliente_nombre} - {self.vehiculo}"
