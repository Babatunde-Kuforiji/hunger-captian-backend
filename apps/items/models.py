from django.db import models
from cloudinary.models import CloudinaryField 
from backend.constants import *
# Create your models here.

class Item(models.Model):
    name=models.CharField('Name',blank=False,null=False,max_length=60,db_index=True)
    
    price = models.DecimalField(
        'Price', blank=False, null=False, max_digits=11, decimal_places=2
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
    status = models.CharField('status',blank=False,db_index=True,max_length=50,choices=STATUS
    
    )
    categories = models.CharField('categories',blank=False,null=False,max_length=50,db_index=True,choices=CATEGORIES)