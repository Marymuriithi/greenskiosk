from django.contrib import admin
from.models import(ShippingProvider, DispenserCoolerBox, Delivery)

# Register your models here.
admin.site.register(ShippingProvider)
admin.site.register(DispenserCoolerBox)
admin.site.register(Delivery)