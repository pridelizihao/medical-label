from django.db import models
import datetime

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)  # 产品名称字段，示例，可根据实际修改
    description = models.TextField()  # 产品描述字段，示例
    author = models.CharField(max_length=100, default='admin')  # 作者字段，示例
    time = models.DateTimeField(default=datetime.datetime.now)    # 时间字段，示例
    image = models.ImageField(upload_to='product_images/')  # 图片字段，指定上传路径
    image_json = models.TextField( null=True, blank=True)  # 图片json字段，示例

    def __str__(self):
        return self.name