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


class Project(models.Model):
    name = models.CharField(max_length=100)
    engineer_responsible = models.ForeignKey(Engineeer, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floors = models.IntegerField()

    materials = models.ManyToManyField(Material, through='ProjectMaterial')
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def update_subtotal(self):
        self.subtotal = sum(pm.quantity * pm.material.price for pm in self.projectmaterial_set.all())
        self.save()


class ProjectMaterial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_value = models.FloatField(default=0)

    def __str__(self):
        return self.project
