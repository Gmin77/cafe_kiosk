from django.contrib import admin
from cafe.models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ('id', 'name')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin) :
    list_display = ('category', 'name', 'price', 'image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin) :
    list_display = ('menu', 'order_date', 'menu_count', 'order_price')
    