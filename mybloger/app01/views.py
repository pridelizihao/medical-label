import base64
from django.shortcuts import render, redirect, reverse, HttpResponse
from app01.forms import ProductForm
from app01.models import Product 
import json


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
    return render(request, 'author/label-interface.html')


 
def image_list(request):
    images = Product.objects.all()
    return render(request, 'image_list.html', {'images': images})

def one(request):
    return render(request, '01.html')

