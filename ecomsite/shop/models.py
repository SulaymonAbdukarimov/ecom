from django.db import models

# Create your models here.
# Product model which you see in official page
class Products(models.Model):
    title = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    discount_price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.title
# Order model which you see this all in ordered products page which you will full in the form   
class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.FloatField()
