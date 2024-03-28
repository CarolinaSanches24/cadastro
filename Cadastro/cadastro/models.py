from django.db import models

# Create your models here.

class Cadastro (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f'{self.name} [{self.email}]'