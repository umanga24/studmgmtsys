from django.contrib import admin

from RedBasket.models import *

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(Orderiteam)


