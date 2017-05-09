from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=50)
    contents = models.TextField()
    
    def __str__(self):
      	return self.productname