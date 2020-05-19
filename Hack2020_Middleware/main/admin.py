from django.contrib import admin
# from django.forms.widgets import TextInput
from .models import  Vessel
# from django_google_maps.widgets import GoogleMapsAddressWidget
# from django_google_maps.fields import AddressField, GeoLocationField

#from main import models


# class MapModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         AddressField: {
#             'widget': GoogleMapsAddressWidget
#         },
#         GeoLocationField: {
#             'widget': TextInput(attrs={
#                 'readonly': 'readonly'
#             })
#         },
#     }
class  HackAdmin(admin.ModelAdmin):
    site_header = 'Welcome to the admin page'



admin.site.register(Vessel)
