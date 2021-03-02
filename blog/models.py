from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.name