from django.contrib import admin

from .models import Captcha, user_head

@admin.register(Captcha)
class CaptchaAdmin(admin.ModelAdmin):
    list_display = ('email','captcha','create_time')
    search_fields = ('email','captcha')
    list_filter = ('create_time',)
    readonly_fields = ('create_time',)  


# Register your models here.
@admin.register(user_head)
class user_headAdmin(admin.ModelAdmin):
    list_display = ('user','head_img')
    search_fields = ('user','head_img')
    list_filter = ('user',)
    readonly_fields = ('user',)  

