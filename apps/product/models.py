import uuid
from django.db import models

from apps.category.models import CategoryModel

# Create your models here.
class ProductModel(models.Model):
    
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    image = models.ImageField(upload_to='images/')
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 8,decimal_places=2)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)