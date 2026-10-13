from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50) 
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Calcetin(models.Model):
    modelo = models.CharField(max_length=100)
    talla = models.CharField(max_length=10)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} - Talla {self.talla}"

class Venta(models.Model):
    calcetin = models.ForeignKey(Calcetin, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()