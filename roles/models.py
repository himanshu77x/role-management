from django.db import models

# Create your models here.
# roles/models.py

from django.db import models
from django.utils import timezone

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=True)  # For soft delete
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name
