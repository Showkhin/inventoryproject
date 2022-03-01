from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = "Showkhin Deshboard"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('staff', 'order_quantity', 'product')
#     list_filter = ('product',)


admin.site.register(Order)
