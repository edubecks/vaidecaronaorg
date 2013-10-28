from django.db import models

# Create your models here.
class CaronaModel(models.Model):
    fb_post_id = models.CharField(max_length=40)
    fb_group_id = models.CharField(max_length=20)
    origin = models.CharField(max_length=30)
    destiny = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=False)
    ofereco_procuro = models.CharField(max_length=1) ## o: ofereco, p: procuro
    num_vagas = models.PositiveSmallIntegerField()


class CaronaGroupModel(models.Model):
    fb_group_id = models.CharField(max_length=20)
    city1 = models.CharField(max_length=30)
    city1_state = models.CharField(max_length=2)
    city1_list = models.CharField(max_length=200)
    city2 = models.CharField(max_length=30)
    city2_state = models.CharField(max_length=2)
    city2_list = models.CharField(max_length=200)


class ParserErrorsModel(models.Model):
    fb_group_id = models.CharField(max_length=20)
    fb_post_id = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)