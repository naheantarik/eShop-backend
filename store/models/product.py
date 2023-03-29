from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', blank=True)
    image = models.ImageField(null=True, blank=True)