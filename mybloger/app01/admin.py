from django.contrib import admin

# Register your models here.
from app01.models import user_image

@admin.register(user_image)
class user_imageAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'user', 'time', 'image', 'image_json']      
    
