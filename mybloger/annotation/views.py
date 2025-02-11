from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse  
from django.views.decorators.http import require_http_methods
from.models import label, rectdata, polygondata, circledata, pencildata
import json
from django.views.decorators.csrf import csrf_exempt
from app01.models import user_image
import datetime
from django.core.files.base import ContentFile
import base64
from PIL import Image
import io

@csrf_exempt
def rectjsondata(request, image_id, type):
    try:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                print(data)
                # 处理接收到的数据
                for i in data:
                    rect = rectdata(
                        image_name=i.get('image_name',"默认name"),
                        text=i.get('text',"默认text"),
                        startx=i.get('startX',0),
                        starty=i.get('startY',0),
                        endx=i.get('endX',100),
                        endy=i.get('endY',100),
                        imageid=user_image.objects.get(id=image_id),
                    )
                    rect.save()
                
                image = user_image.objects.get(id=image_id)
                if type == 1:
                    image.islabeled = True
                elif type == 2:
                    image.isailabeled = True
                image.time = datetime.datetime.now()
                image.save()
                return HttpResponse("success")
            except Exception as e:
                # 处理 JSON 解析错误或 rect 保存错误
                print(f"Error occurred while processing data: {str(e)}")
                return HttpResponse(f"Error: {str(e)}", status=500)
        else:
            return HttpResponse("error")
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON data", status=400)

    
def circlejsonndata(request, image_id, type):
    try:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                print(data)
                # 处理接收到的数据
                for i in data:
                    circle = circledata(
                        image_name=i.get('image_name',"默认name"),
                        text=i.get('text',"默认text"),
                        x=i.get('X',0),
                        y=i.get('Y',0),
                        r=i.get('R',10),
                        imageid=user_image.objects.get(id=image_id),
                    )
                    circle.save()
                
                image = user_image.objects.get(id=image_id)
                if type == 1:
                    image.islabeled = True
                elif type == 2:
                    image.isailabeled = True
                image.time = datetime.datetime.now()
                image.save()
                return HttpResponse("success")
            except Exception as e:
                # 处理 JSON 解析错误或 circle 保存错误
                print(f"Error occurred while processing data: {str(e)}")
                return HttpResponse(f"Error: {str(e)}", status=500)
        else:
            return HttpResponse("error")
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON data", status=400)

    
def polygonjsonndata(request, image_id, type):
    try:
        if request.method == 'POST':
            try:    
                data = json.loads(request.body)
                print(data)
                # 处理接收到的数据
                for i in data:
                    polygon = polygondata(
                        image_name=i.get('image_name',"默认name"),
                        text=i.get('text',"默认text"),
                        polygon=i.get('points',[[0,0],[100,0],[100,100],[0,100]]),
                        imageid=user_image.objects.get(id=image_id),
                    )
                    polygon.save()

                image = user_image.objects.get(id=image_id)
                if type == 1:
                    image.islabeled = True
                elif type == 2:
                    image.isailabeled = True
                image.time = datetime.datetime.now()
                image.save()
                return HttpResponse("success")
            except Exception as e:
                # 处理 JSON 解析错误或 polygon 保存错误
                print(f"Error occurred while processing data: {str(e)}")
                return HttpResponse(f"Error: {str(e)}", status=500)
        else:
            return HttpResponse("error")
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON data", status=400)

def penciljsondata(request, image_id, type):
    try:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                print(data)
                # 处理接收到的数据
                for i in data:
                    pencil = pencildata(
                        image_name=i.get('image_name',"默认name"),
                        text=i.get('text',"默认text"),
                        pencil=i.get('points',[[0,0],[100,0],[100,100],[0,100]]),
                        imageid=user_image.objects.get(id=image_id),
                    )
                    pencil.save()

                image = user_image.objects.get(id=image_id)
                if type == 1:
                    image.islabeled = True
                elif type == 2:
                    image.isailabeled = True
                image.time = datetime.datetime.now()
                image.save()
                return HttpResponse("success")
            except Exception as e:
                # 处理 JSON 解析错误或 pencil 保存错误
                print(f"Error occurred while processing data: {str(e)}")
                return HttpResponse(f"Error: {str(e)}", status=500)
        else:
            return HttpResponse("error")
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON data", status=400)

@csrf_exempt
def saveimage(request, image_id):
    if request.method == 'POST':
        # 使用 request.POST 获取 Base64 编码的图片数据
        image_data = request.POST.get('image_data')
        
        if image_data:
            try:
                # 去除 Base64 编码的前缀
                data = image_data.split(',')[1]
                # 解码 Base64 数据
                image_bytes = base64.b64decode(data)
                # 使用 PIL 打开图片
                image = Image.open(io.BytesIO(image_bytes))
                
                # 将图像数据转换为 ContentFile 对象
                buffer = io.BytesIO()
                image.save(buffer, format="PNG")
                file_content = ContentFile(buffer.getvalue())
                
                # 获取对应的 user_image 实例
                original = user_image.objects.get(id=image_id)
                # 将 ContentFile 对象赋值给模型的 image 字段
                original.image.save(f'{original.name}.png', file_content)
                original.save()
                
                print("image saved")
                return HttpResponse("success")
            except user_image.DoesNotExist:
                print(f"user_image with id {image_id} does not exist.")
                return HttpResponse("error: image not found", status=404)
            except Exception as e:
                print(f"An error occurred: {e}")
                return HttpResponse("error: internal server error", status=500)
        else:
            print("image data is empty")
            return HttpResponse("error: no image data", status=400)
    else:
        print("not a post request")
        return HttpResponse("error: only POST requests are allowed", status=405)
    
def label_list(request):
    labels = label.objects.all()
    return JsonResponse({'labels': [label.name for label in labels]})

def image_rect_json(request, image_id):
    rects = rectdata.objects.filter(id=image_id)
    return JsonResponse({'rects': [{'text': rect.text, 'label_id': rect.label_id.id, 'startx': rect.startx, 'starty': rect.starty, 'endx': rect.endx, 'endy': rect.endy} for rect in rects]})

def image_circle_json(request, image_id):
    circles = circledata.objects.filter(id=image_id)
    return JsonResponse({'circles': [{'text': circle.text, 'label_id': circle.label_id.id, 'x': circle.x, 'y': circle.y, 'r': circle.r} for circle in circles]})

def image_polygon_json(request, image_id):
    polygons = polygondata.objects.filter(id=image_id)
    return JsonResponse({'polygons': [{'text': polygon.text, 'label_id': polygon.label_id.id, 'polygon': polygon.polygon} for polygon in polygons]})    

def delete_rect(request, rect_id):
    rect = get_object_or_404(rectdata, id=rect_id)
    rect.delete()
    return HttpResponse("success")

def delete_circle(request, circle_id):
    circle = get_object_or_404(circledata, id=circle_id)
    circle.delete()
    return HttpResponse("success")

def delete_polygon(request, polygon_id):
    polygon = get_object_or_404(polygondata, id=polygon_id)
    polygon.delete()
    return HttpResponse("success")  

def labeledshow(request, image_id):
    image = get_object_or_404(user_image, id=image_id)
    rectjsondata = rectdata.objects.filter(imageid=image_id)
    circlejsondata = circledata.objects.filter(imageid=image_id)
    polygonjsondata = polygondata.objects.filter(imageid=image_id)
    penciljsondata = pencildata.objects.filter(imageid=image_id)
    return render(request, 'labeledshow.html',{'image': image, 'rectjsondata': rectjsondata, 'circlejsondata': circlejsondata, 'polygonjsondata': polygonjsondata, 'penciljsondata': penciljsondata})