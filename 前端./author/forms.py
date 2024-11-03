from django import forms
from django.contrib.auth import get_user_model
from .models import Captcha

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        min_length=4, 
        label='用户名' ,
        error_messages={'required': '用户名不能为空', 'invalid': '用户名格式错误'}
        )
    email = forms.EmailField(
        max_length=100,
        label='邮箱' ,
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'}
        )
    captcha = forms.CharField(
        max_length=4,
        min_length=4, 
        label='验证码' ,
        error_messages={'required': '验证码不能为空', 'invalid': '验证码格式错误'}
        )
    password = forms.CharField(
        max_length=100,
        min_length=6, 
        label='密码' ,
        error_messages={'required': '密码不能为空', 'invalid': '密码格式错误'}
        )

    def clean_email(self):  
        email = self.cleaned_data.get('email')  
        exist =User.objects.filter(email=email).exists()
        if exist:   
            raise forms.ValidationError('邮箱已被注册')  
        return email
    
    def clean_captcha(self):  
        captcha = self.cleaned_data.get('captcha')  
        email = self.cleaned_data.get('email')  
        captcha_model = Captcha.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:  
            raise forms.ValidationError('验证码错误')  
        captcha_model.delete()  
        return captcha
