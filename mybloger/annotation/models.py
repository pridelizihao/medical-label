from django.db import models
import datetime
from app01 import models as app01_models

class label(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True) 

class rectdata(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    startx = models.IntegerField()
    starty = models.IntegerField()
    endx = models.IntegerField()
    endy = models.IntegerField()
    label_id = models.ForeignKey(label, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class polygondata(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    # 多边形的各个顶点坐标
    polygon = models.TextField(("Polygon"))
    label_id = models.ForeignKey(label, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class circledata(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    x = models.IntegerField()
    y = models.IntegerField()
    r = models.IntegerField()
    label_id = models.ForeignKey(label, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

  

