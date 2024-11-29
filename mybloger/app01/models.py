from django.db import models

# Create your models here.
class Base64Image(models.Model):
    title = models.CharField(max_length=100)
    image_data = models.TextField()  # 用于存储base64编码的图片数据
 
    def __str__(self):
        return self.title