from django.db import models

class Estudios(models.Model):
    lenguaje = models.CharField(max_length=20)
    duracion = models.CharField(max_length=20)
    nota = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.lenguaje} {self.nota}'
    
    