from django.contrib import admin

# Register your models here.
from app01.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'image_json')   
    
