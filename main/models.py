from django.db import models

# Create your models here.

CATEGORY=(
    ('None','None'),
    ('DVD','DVD'),
    ('Book','Book'),
    ('Furniture','Furniture')
)


class Products(models.Model):
    sku = models.CharField(max_length=5,unique=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=True)
    category = models.CharField(max_length=100,choices=CATEGORY,default='None')
    size = models.CharField(max_length=50)