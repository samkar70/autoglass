from django.shortcuts import render, redirect, get_object_or_404
from .models import Orden
from .forms import OrdenForm
import math # <-- AÑADE ESTA LÍNEA

# --- NUEVA FUNCIÓN PARA CALCULAR DISTANCIA ---
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Convertir de grados a radianes
    R = 3958.8 # Radio de la Tierra en millas
    rlat1 = math.radians(lat1)
    rlon1 = math.radians(lon1)
    rlat2 = math.radians(lat2)
    rlon2 = math.radians(lon2)

    dlon = rlon2 - rlon1
    dlat = rlat2 - rlat1

    a = math.sin(dlat / 2)**2 + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c
    return round(distancia, 2) # Redondea a 2 decimales

# --- VISTAS (La única que cambia es registrar_viaje) ---

def lista_ordenes(request):
    # ... (sin cambios)
    ordenes = Orden.objects.all()
    return render(request, 'ordenes/lista_ordenes.html', {'ordenes': ordenes})

def crear_orden(request):
    # ... (sin cambios)
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes')
    else:
        form = OrdenForm()
    return render(request, 'ordenes/crear_orden.html', {'form': form})

def detalle_orden(request, orden_id):
    # ... (sin cambios)
    orden = get_object_or_404(Orden, pk=orden_id)
    return render(request, 'ordenes/detalle_orden.html', {'orden': orden})

def editar_orden(request, orden_id):
    # ... (sin cambios)
    orden = get_object_or_404(Orden, pk=orden_id)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('detalle_orden', orden_id=orden.id)
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'ordenes/editar_orden.html', {'form': form, 'orden': orden})

def eliminar_orden(request, orden_id):
    # ... (sin cambios)
    orden = get_object_or_404(Orden, pk=orden_id)
    if request.method == 'POST':
        orden.delete()
        return redirect('lista_ordenes')
    return render(request, 'ordenes/eliminar_orden.html', {'orden': orden})

# --- VISTA registrar_viaje ACTUALIZADA ---
# En ordenes/views.py, reemplaza esta función:

def registrar_viaje(request, orden_id):
    orden = get_object_or_404(Orden, pk=orden_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        latitud_str = request.POST.get('latitud')
        longitud_str = request.POST.get('longitud')

        if action == 'iniciar' and latitud_str and longitud_str:
            orden.latitud_inicio = latitud_str
            orden.longitud_inicio = longitud_str
            orden.save()

        elif action == 'finalizar' and latitud_str and longitud_str:
            orden.latitud_fin = latitud_str
            orden.longitud_fin = longitud_str

            # ¡Aquí está la corrección!
            # Nos aseguramos de que todos los números sean 'float' antes de calcular.
            if orden.latitud_inicio and orden.longitud_inicio:
                distancia = calcular_distancia(
                    float(orden.latitud_inicio),
                    float(orden.longitud_inicio),
                    float(orden.latitud_fin),
                    float(orden.longitud_fin)
                )
                orden.millaje_recorrido = distancia

            orden.save()

    return redirect('detalle_orden', orden_id=orden.id)
