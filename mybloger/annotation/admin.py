from django.contrib import admin
from.models import  label,rectdata,circledata,polygondata

# Register your models here.
@admin.register(rectdata)
class rectdataAdmin(admin.ModelAdmin):
    list_display =  ('id', 'label_id', 'image_name', 'text','startx','starty', 'endx', 'endy', 'create_time') 
    list_filter = ('label_id', "id")
    search_fields = ('label_id', "id")

@admin.register(circledata)
class circledataAdmin(admin.ModelAdmin):
    list_display =  ('id', 'label_id', 'image_name', 'text', 'x', 'y', 'r', 'create_time') 
    list_filter = ('label_id', "id")
    search_fields = ('label_id', "id")

@admin.register(polygondata)
class polygondataAdmin(admin.ModelAdmin):
    list_display =  ('id', 'label_id','image_name', 'text', 'polygon', 'create_time') 
    list_filter = ('label_id', "id")
    search_fields = ('label_id', "id")

@admin.register(label)
class labelAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name', 'create_time', 'update_time') 
    list_filter = ('name',"id")
    search_fields = ('name', "id")


