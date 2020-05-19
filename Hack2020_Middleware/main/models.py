from django.db import models
from django.contrib.auth.models import User
# from django_google_maps.fields import AddressField, GeoLocationField



# Create your models here.
class Vessel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vesselLength = models.IntegerField()
    vesselBreadth = models.IntegerField()
    vesselMaxDraft = models.IntegerField()
    vesselSpeed = models.IntegerField()
    vesselName = models.CharField(max_length=100)

# class Map(models.Model):
#     geolocation = GeoLocationField(blank=True)
#     address = AddressField(max_length=100)
#     def __str__(self):
#         return self.address

    #lon = models.DecimalField(max_digits= 10,decimal_places=6)
    #lat = models.DecimalField(max_digits= 10,decimal_places=6)
    #vessel = models.ForeignKey(Vessel,on_delete=models.SET_NULL, null=True)
