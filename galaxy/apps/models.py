from django.db import models
from cloudinary.models import CloudinaryField

class App(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    apk_file = models.BinaryField(blank=True, null=True)  
    apk_filename = models.CharField(max_length=200, blank=True) 
    image = CloudinaryField('image', blank=True, null=True)  
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
