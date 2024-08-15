from django.contrib import admin

# Register your models here.
from .models import order,order_items
admin.site.register(order)
admin.site.register(order_items)