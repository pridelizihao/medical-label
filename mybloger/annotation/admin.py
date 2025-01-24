from django.contrib import admin
from.models import  label,rectdata,circledata,polygondata,pencildata

# Register your models here.
@admin.register(rectdata)
class rectdataAdmin(admin.ModelAdmin):
    list_display =  ('id' ,'image_name', 'text','startx','starty', 'endx', 'endy', 'create_time') 

@admin.register(circledata)
class circledataAdmin(admin.ModelAdmin):
    list_display =  ('id','image_name', 'text', 'x', 'y', 'r', 'create_time') 


@admin.register(polygondata)
class polygondataAdmin(admin.ModelAdmin):
    list_display =  ('id', 'image_name', 'text', 'polygon', 'create_time') 

@admin.register(pencildata)
class pencildataAdmin(admin.ModelAdmin):
    list_display =  ('id', 'image_name', 'text', "pencil", 'create_time') 
 

@admin.register(label)
class labelAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name', 'create_time', 'update_time') 
    list_filter = ('name',"id")
    search_fields = ('name', "id")


