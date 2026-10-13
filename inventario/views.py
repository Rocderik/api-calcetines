from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Calcetin
import json

# Vista Web
def listar_calcetines(request):
    calcetines = Calcetin.objects.all()
    return render(request, 'lista_calcetines.html', {'calcetines': calcetines})

# Vistas API REST
@csrf_exempt
def api_calcetines(request):
    if request.method == 'GET':
        calcetines = list(Calcetin.objects.values('id', 'modelo', 'talla', 'precio', 'stock', 'categoria_id'))
        return JsonResponse(calcetines, safe=False)
        
    elif request.method == 'POST':
        data = json.loads(request.body)
        nuevo_calcetin = Calcetin.objects.create(
            modelo=data['modelo'],
            talla=data['talla'],
            precio=data['precio'],
            stock=data['stock'],
            categoria_id=data['categoria_id']
        )
        return JsonResponse({'mensaje': 'Calcetín creado', 'id': nuevo_calcetin.id}, status=201)

@csrf_exempt
def api_calcetin_detalle(request, pk):
    try:
        calcetin = Calcetin.objects.get(pk=pk)
    except Calcetin.DoesNotExist:
        return JsonResponse({'error': 'Calcetín no encontrado'}, status=404)

    if request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        calcetin.modelo = data.get('modelo', calcetin.modelo)
        calcetin.talla = data.get('talla', calcetin.talla)
        calcetin.precio = data.get('precio', calcetin.precio)
        calcetin.stock = data.get('stock', calcetin.stock)
        calcetin.save()
        return JsonResponse({'mensaje': 'Calcetín actualizado'})

    elif request.method == 'DELETE':
        calcetin.delete()
        return JsonResponse({'mensaje': 'Calcetín eliminado'})
