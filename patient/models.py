from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

