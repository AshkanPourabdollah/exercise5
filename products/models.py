from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(default='',max_length=30)
    price = models.IntegerField(default=0)
    details = models.CharField(default='',max_length=500)

    def __str__(self):
        return self.title