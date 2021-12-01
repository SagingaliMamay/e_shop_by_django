from django.db import models

# Create your models here.

#1 Category:
#2 Product
#3 CartProduct
#4 Cart
#5 Order
#6 Customer
#7 Description/Specification

# Here I create my first model by class


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of Category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
# Second model
class Product(models.Model):
    category = models.CharField(max_length=255, verbose_name='Category',  on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Name of product')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Images')
    description = models.TextField(verbose_name='Description', null=True)#<-- null = True means that this filed can be empty
    price = models.TextField(max_digits=9, decimal_places=2, verbose_name='price')

    def __str__(self):
        return self.title
#Third model

class CartProduct(models.Model):
