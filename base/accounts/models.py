from django.db import models
from django.contrib.auth.models import User

class DatoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='accounts', blank=True, null=True)
    def __str__(self):
        return f'{self.user.username} - DatoExtra'
