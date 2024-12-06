from django.db import models

# Create your models here.
class Base64Image(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name="图片", default='default.jpg')
    image_data = models.TextField(verbose_name="图片数据")  # 用于存储base64编码的图片数据
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    def __str__(self):
        return self.title