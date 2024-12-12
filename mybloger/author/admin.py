from django.contrib import admin

from .models import Captcha

@admin.register(Captcha)
class CaptchaAdmin(admin.ModelAdmin):
    list_display = ('email','captcha','create_time')
    search_fields = ('email','captcha')
    list_filter = ('create_time',)
    readonly_fields = ('create_time',)  

