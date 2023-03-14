from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    class Meta():
        db_table = 'admin'

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=20)

    class Meta():
        db_table = 'products'

class Size(models.Model):
    size = models.BigIntegerField()

    class Meta():
        db_table = 'size'


class Variants(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    quantity = models.BigIntegerField()

    class Meta():
        db_table = 'variants'