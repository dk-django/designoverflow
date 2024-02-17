from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ProductImageGenerator(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=4000)
    product_image = models.ImageField(upload_to='product-images/')

    def __str__(self):
        return self.prompt
    