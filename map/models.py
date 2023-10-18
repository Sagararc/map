from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} - Latitude: {self.latitude}, Longitude: {self.longitude}"


class FormModel(models.Model):    
    name = models.CharField(max_length=100,blank=True , null=True)
    mobile = models.CharField(max_length=100,blank=True , null=True)
    mail = models.CharField(max_length=100 , blank=True , null=True)
    city = models.CharField(max_length=100 , blank=True , null=True)
    counts = models.CharField(max_length=100 , blank=True , null=True)
    def __str__(self):
        return self.name