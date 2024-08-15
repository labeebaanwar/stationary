from django.db import models

# Create your models here.
class site_settings(models.Model):
    image=models.ImageField(upload_to='media/theme')
    caption=models.TextField()
