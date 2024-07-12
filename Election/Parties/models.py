from django.db import models
from PIL import Image
# Create your models here.


class Party(models.Model):
    name = models.CharField(max_length=100)
    propaganda = models.TextField()
    logo = models.ImageField(default='default.jpeg', upload_to='party_logos', max_length=255) 
    votes = models.IntegerField(default=0)
    president = models.CharField(max_length=100)
    vicepresident = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        logo = Image.open(self.logo.path)
        if logo.height > 300 or logo.width > 300:
            output_size = (300, 300)
            logo.thumbnail(output_size)
            logo.save(self.logo.path)