from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=200)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    statistics = models.IntegerField(default=0)