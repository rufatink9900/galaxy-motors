from django.db import models

class App(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    apk_file = models.BinaryField(blank=True, null=True)  
    apk_filename = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.name
