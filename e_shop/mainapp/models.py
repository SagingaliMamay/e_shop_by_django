from django.db import models


# Create your models here.

# 1 Category:
# 2 Product
# 3 CartProduct
# 4 Cart
# 5 Order
# 6 Customer
# 7 Description/Specification

# Here I create my first model by class


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of Category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# Second model
class Product(models.Model):
    category = models.CharField(max_length=255, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Name of product')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Images')
    description = models.TextField(verbose_name='Description',
                                   null=True)  # <-- null = True means that this filed can be empty
    price = models.TextField(max_digits=9, decimal_places=2, verbose_name='price')

    # Representetion of  this  class in my admin panel

    def __str__(self):
        return self.title


# Third model

class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Final Price')

    def __str__(self):
        return "Cart product: {} (for cart)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    products = modelsManyToManyField(CartProduct, blank=True)
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Final Price')

    def __str__(self):
        return str(self.id)

