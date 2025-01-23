from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse  
from django.views.decorators.http import require_http_methods
from.models import label, rectdata, polygondata, circledata, pencildata
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def rectjsondata(request):
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
                    )
                    rect.save()
                return HttpResponse("success")
            except Exception as e:
                # 处理 JSON 解析错误或 rect 保存错误
                print(f"Error occurred while processing data: {str(e)}")
                return HttpResponse(f"Error: {str(e)}", status=500)
        else:
            return HttpResponse("error")
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON data", status=400)

    
def circlejsonndata(request):
    if request.is_json():
        data = request.get_json()
        # do something with the data
        for i in data:
            circle = circledata(
                image_name=i['image_name'],
                text=i['text'],
                x=i['x'],
                y=i['y'],
                r=i['r'],
                label_id=i['label_id']
            )
            circle.save()
        return HttpResponse("success")
    else:
        return HttpResponse("error")

    
def polygonjsonndata(request):
    if request.is_json():
        data = request.get_json()
        # do something with the data
        for i in data:
            polygon = polygondata(
                image_name=i['image_name'],
                text=i['text'],
                polygon=i['polygon'],
                label_id=i['label_id']
            )
            polygon.save()
        return HttpResponse("success")
    else:
        return HttpResponse("error")

def penciljsondata(request):
    if request.is_json():
        data = request.get_json()
        # do something with the data
        for i in data:
            pencil = pencildata(
                image_name=i['image_name'],
                text=i['text'],
                x=i['x'],
                y=i['y'],
                label_id=i['label_id']
            )
            pencil.save()
        return HttpResponse("success")
    else:
        return HttpResponse("error")
    
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

