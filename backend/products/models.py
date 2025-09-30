from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=6)
    stock = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name
