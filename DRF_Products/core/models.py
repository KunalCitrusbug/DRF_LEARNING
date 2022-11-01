from django.db import models


# BRAND
class Brand(models.Model):
    brand = models.CharField(max_length=100,)


# PRODUCTS
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='brand_fk')

    def __str__(self):
        return self.name
