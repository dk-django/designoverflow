from django.contrib.auth.models import User
from django.db import models

class DalleGeneration(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    user_prompt = models.TextField()
    dalle_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # product_image = models.ImageField(upload_to='product-images/')

    def __str__(self):
        return f"{self.user_prompt} - {self.created_at}"

    class Meta: 
       ordering = ['dalle_response'] 
    