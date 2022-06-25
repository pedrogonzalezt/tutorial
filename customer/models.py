from django.db import models

class Customer(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(null=True)
    direccion = models.CharField('Direccion', max_length=240, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name