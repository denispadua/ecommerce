import uuid
from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    cpf = models.CharField(max_length=11)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.full_name