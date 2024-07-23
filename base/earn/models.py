from django.db import models

class Monedas(models.Model):
    nombre = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='monedas/')
    
    def __str__(self):
        return f'{self.nombre} {self.valor}'