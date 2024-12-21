import base64
from django.shortcuts import render, redirect, reverse, HttpResponse
from app01.forms import UserImageForm, UserImageForm2
from app01.models import user_image
import json
from django.contrib.auth.decorators import login_required
from author.models import user_head
from django.conf import settings
from django.contrib import messages
import os
from django.db import transaction
import datetime


@login_required
def create_product(request):
    if request.method == 'POST':
        form1 = UserImageForm(request.POST, request.FILES)  # 注意要传递request.FILES来接收文件数据
        form2 = UserImageForm2(request.POST, request.FILES)
        user = request.user
        if form1.is_valid():
            json_data = json.dumps({'success': True})  # 假设成功，返回json数据
            form1.instance.user = user  # 给表单实例绑定用户信息
            form1.save()  # 保存表单数据到模型，同时图片会被存储到指定路径
            return redirect(reverse('app01:upload_image'))  # 假设成功后重定向到产品列表页面，需根据实际配置
        if form2.is_valid():
            folders = request.FILES.getlist('folder')  # 获取所有上传的文件列表
            user = request.user
            base_upload_path = os.path.join('media', 'product_image2')
            os.makedirs(base_upload_path, exist_ok=True)

            for folder in folders:
                file_name = os.path.basename(folder.name)
                file_extension = os.path.splitext(file_name)[1].lower()
                if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                    destination_path = os.path.join(base_upload_path, file_name)
                    with open(destination_path, 'wb') as destination_file:
                        for chunk in folder.chunks():
                            destination_file.write(chunk)

                    # 将图片相关信息保存到数据库
                    new_image = user_image(
                        user=user,
                        name=os.path.splitext(file_name)[0],
                        author=user.username if user.username else 'admin',
                        time=datetime.datetime.now(),
                        image=os.path.join('product_image2', file_name),
                    )
                    new_image.save()
            return redirect(reverse('app01:upload_image'))  # 假设成功后重定向到产品列表页面，需根据实际配置'app01:upload_image')
        else:
            return HttpResponse("表单验证失败，请检查填写的信息")
    else:
        form1 = UserImageForm()
        form2 = UserImageForm2()
    return render(request, 'upload_product.html', {'form1': form1,"form2":form2})


@login_required
def upload_folder(request):
    if request.method == 'POST':
        form2 = UserImageForm2(request.POST, request.FILES)
        if form2.is_valid():
            folders = request.FILES.getlist('folder')  # 获取所有上传的文件列表
            user = request.user
            base_upload_path = os.path.join('media', 'product_image2')
            os.makedirs(base_upload_path, exist_ok=True)

            for folder in folders:
                file_name = os.path.basename(folder.name)
                file_extension = os.path.splitext(file_name)[1].lower()
                if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                    destination_path = os.path.join(base_upload_path, file_name)
                    with open(destination_path, 'wb') as destination_file:
                        for chunk in folder.chunks():
                            destination_file.write(chunk)

                    # 将图片相关信息保存到数据库
                    new_image = user_image(
                        user=user,
                        name=os.path.splitext(file_name)[0],
                        author=user.username if user.username else 'admin',
                        time=datetime.datetime.now(),
                        image=os.path.join('product_image2', file_name),
                    )
                    new_image.save()
                    print(f"保存图片 {file_name} 相关信息到数据库成功")
            return redirect(reverse('app01:upload_image'))  # 假设成功后重定向到产品列表页面，需根据实际配置'app01:upload_image')
        else:
            return HttpResponse("表单验证失败，请检查填写的信息")
    else:
        form2 = UserImageForm2()
    return render(request, 'upload_product2.html', {'form2': form2})

def label(request):
    return render(request, 'label-interface.html')

def person(request):
    return render(request, 'person.html')

def home(request):
    num1 = user_image.objects.filter(user_id = request.user.id).count()
    num2 = user_image.objects.filter(user_id = request.user.id, islabeled=True).count()
    num3 = user_image.objects.filter(user_id = request.user.id, isailabeled=True).count()
    return render(request, 'home.html',{'num1':num1,'num2':num2,'num3':num3})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html',{'user':user})


@login_required
def edit_profile(request):
 return render(request, 'edit_profile.html')

@login_required
def image_list(request):
    images = user_image.objects.filter(user_id = request.user.id, islabeled=False, isailabeled=False)
    return render(request, 'image_list.html', {'images': images})

def image_labeled(request):
    images = user_image.objects.filter(user_id = request.user.id, islabeled=True)
    return render(request, 'image_labeled.html', {'images': images})

def image_ailabeled(request):
    images = user_image.objects.filter(user_id = request.user.id, isailabeled=True)
    return render(request, 'image_ailabeled.html', {'images': images})


@login_required
def delete_image(request, image_id):
    image = user_image.objects.get(id=image_id)
    image.delete()
    messages.success(request, '删除成功')
    return redirect(reverse('app01:image_list'))

@login_required
def annotate_image(request, image_id):
    image = user_image.objects.get(id=image_id)
    return render(request, 'annotate_image.html', {'image': image})

def page(request):
    return render(request, '1.html')

def page2(request):
    return render(request, '01.html')