from django.db import models
from app01 import models as app01_models

class label(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True) 

class Annotation(models.Model):
    id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=20)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    label = models.ForeignKey(label, on_delete=models.CASCADE)
    image = models.ForeignKey(app01_models.Product, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)   

  

