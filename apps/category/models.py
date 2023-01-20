import uuid
from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name