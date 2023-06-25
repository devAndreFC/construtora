from django.db import models


class Engineeer(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    crea = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    measure = models.CharField(default='U', max_length=1, choices=(
        ('U', 'Unidade'), ('C', 'Caixa'), ('M', 'Metro'), ('L', 'Litro'),))
    price = models.FloatField(verbose_name='Preço', default=0)

    def __str__(self):
        return self.name
