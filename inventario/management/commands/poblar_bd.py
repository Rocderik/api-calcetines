from django.core.management.base import BaseCommand
from inventario.models import Categoria, Calcetin

class Command(BaseCommand):
    help = 'Puebla la base de datos con semillas para la tienda de calcetines'

    def handle(self, *args, **kwargs):
        # 1. Crear Categorías
        cat_deportiva, created = Categoria.objects.get_or_create(
            nombre='Deportivos',
            descripcion='Calcetines transpirables para alto rendimiento y ejercicio.'
        )
        cat_formal, created = Categoria.objects.get_or_create(
            nombre='Formales',
            descripcion='Colores sobrios y materiales premium para la oficina.'
        )
        cat_divertida, created = Categoria.objects.get_or_create(
            nombre='Divertidos',
            descripcion='Diseños extravagantes, colores vivos y temáticas de cultura pop.'
        )

        self.stdout.write('Categorías creadas...')

        # 2. Crear Calcetines
        Calcetin.objects.get_or_create(
            modelo='Runner Pro X',
            talla='M',
            precio=4500,
            stock=50,
            categoria=cat_deportiva
        )
        Calcetin.objects.get_or_create(
            modelo='Ejecutivo Classic Black',
            talla='L',
            precio=6000,
            stock=20,
            categoria=cat_formal
        )
        Calcetin.objects.get_or_create(
            modelo='Gatos en el Espacio',
            talla='S',
            precio=3500,
            stock=15,
            categoria=cat_divertida
        )
        Calcetin.objects.get_or_create(
            modelo='Cycling Aerodynamic',
            talla='L',
            precio=5500,
            stock=8,
            categoria=cat_deportiva
        )
        Calcetin.objects.get_or_create(
            modelo='Pizzas Flotantes',
            talla='M',
            precio=3500,
            stock=100,
            categoria=cat_divertida
        )

        # Mensaje de éxito en la terminal
        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente con las semillas!'))