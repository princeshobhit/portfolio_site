from django.db import models

# Create your models here.
class Jobs(models.Model):
    image = models.ImageField(upload_to='images_files/')
    summary = models.CharField(max_length=200)

