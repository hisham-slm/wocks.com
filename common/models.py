from django.db import models

from wocks_admin.models import Product


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta():
        db_table = 'customer'

class Review(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('wocks_admin.Product', on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

    class Meta():
        db_table = 'review'


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()

    class Meta:
        db_table = 'cart'