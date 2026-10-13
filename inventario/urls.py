from django.urls import path
from . import views

urlpatterns = [
    # Rutas Web
    path('', views.listar_calcetines, name='web_calcetines'),
    
    # Rutas API REST
    path('api/calcetines/', views.api_calcetines, name='api_calcetines'),
    path('api/calcetines/<int:pk>/', views.api_calcetin_detalle, name='api_calcetin_detalle'),
]