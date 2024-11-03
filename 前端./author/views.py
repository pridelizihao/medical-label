from django.shortcuts import render,redirect
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail
from .models import Captcha
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm
from django.contrib.auth import get_user_model 

User = get_user_model()

# Create your views here.
def login(request):
    return render(request, 'html/login.html')

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'html/register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return render(request, 'html/login.html')
        else:
            print(form.errors)
            return render(request, 'html/register.html', {'form': form})
            

def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400,'msg': '邮箱不能为空'})
    # 发送验证码
    # 验证码有效期10分钟
    # 验证码内容为4位数字
    # 验证码发送成功后，返回验证码内容  
    # 前端根据返回的验证码内容进行验证
    # 验证成功后，显示发送成功页面
    # 验证失败后，显示发送失败页面
    captcha = ''.join(random.sample(string.digits, 4))
    Captcha.objects.update_or_create(email=email, defaults={'captcha': captcha})
    
    send_mail(
        subject='验证码',
        message='您的验证码为：' + captcha,
        recipient_list=[email],
        fail_silently=False,
        from_email='pridelizihao@foxmail.com'

    )
    return JsonResponse({'code': 200, "msg": "验证码发送成功"})    
 