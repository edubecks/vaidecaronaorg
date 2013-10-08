from django.db import models

# Create your models here.
class Carona(models.Model):
    origin = models.CharField(max_length=30)
    destiny = models.CharField(max_length=30)
    date = models.DateTimeField()
    ofereco_procuro = models.CharField(max_length=1) ## o: ofereco, p: procuro
    num_vagas = models.PositiveSmallIntegerField()