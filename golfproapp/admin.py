from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(inv_options)
admin.site.register(inventory)
admin.site.register(order)
admin.site.register(OrderItem)
admin.site.register(Golfing)