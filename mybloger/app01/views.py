import base64
from django.shortcuts import render, redirect, reverse, HttpResponse
from app01.forms import ProductForm
from app01.models import Product 
import json
from django.contrib.auth.decorators import login_required
from author.models import user_head
from django.conf import settings
import os

from.forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # 注意要传递request.FILES来接收文件数据
        if form.is_valid():
            json_data = json.dumps({'success': True})  # 假设成功，返回json数据
            form.save()  # 保存表单数据到模型，同时图片会被存储到指定路径
            return redirect(reverse('app01:upload_image'))  # 假设成功后重定向到产品列表页面，需根据实际配置
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

def label(request):
    return render(request, 'label-interface.html')

def person(request):
    return render(request, 'person.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html',{'user':user})


def edit_profile(request):
    # 处理GET请求
    if request.method == 'GET':
        return render(request, 'edit_profile.html')
    # 处理POST请求
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_avatar = request.FILES.get('avatar')
        user_profile = user_head.objects.get(user=request.user)
        # 更新姓名
        # 如果有新头像上传，处理头像更新
        if new_avatar:
            # 删除旧头像文件（如果存在）
            if user_profile.head_img:
                old_avatar_path = os.path.join(settings.MEDIA_ROOT, user_profile.avatar.name)
                if os.path.exists(old_avatar_path):
                    os.remove(old_avatar_path)
            user_profile.head_img = new_avatar

        user_profile.save()
        return redirect('profile')  # 保存成功后重定向到个人资料页面

    user_profile = user_head.objects.get(user=request.user)
    return render(request, 'edit_profile.html', {'user_profile': user_profile})


def image_list(request):
    images = Product.objects.all()
    return render(request, 'image_list.html', {'images': images})

def one(request):
    return render(request, '01.html')

