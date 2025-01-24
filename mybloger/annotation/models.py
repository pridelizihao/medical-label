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
    image_name = models.CharField(max_length=200,default='默认名字')
    text = models.CharField(max_length=200,default='默认数据')
    # 设置默认数据
    startx = models.IntegerField(default=0)
    starty = models.IntegerField(default=0)
    endx = models.IntegerField(default=100)
    endy = models.IntegerField(default=100)
    create_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return "(%s, %s, %s, %s, %s, %s, %s, %s)" % (self.id, self.image_name, self.text, self.startx, self.starty, self.endx, self.endy, self.create_time)          

class polygondata(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    # 多边形的各个顶点坐标
    polygon = models.TextField(("Polygon"))
    create_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return "(%s, %s, %s, %s, %s)" % (self.id, self.image_name, self.text, self.polygon, self.create_time)          

class circledata(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    x = models.IntegerField()
    y = models.IntegerField()
    r = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return "(%s, %s, %s, %s, %s, %s, %s)" % (self.id, self.image_name, self.text, self.x, self.y, self.r, self.create_time)          

  
class pencildata(models.Model):
    id = models.AutoField(primary_key=True) 
    image_name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    pencil = models.TextField(("Pencil"))
    create_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.id, self.image_name, self.pencil, self.text)          
