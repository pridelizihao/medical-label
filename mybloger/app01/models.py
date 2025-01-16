from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class user_image(models.Model):
    name = models.CharField(max_length=100)  # 产品名称字段，示例，可根据实际修改
    author = models.CharField(max_length=100, default='admin')  # 作者字段，示例
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  # 用户外键字段，示例
    time = models.DateTimeField(default=datetime.datetime.now)    # 时间字段，示例
    image = models.ImageField(upload_to='product_images/')  # 图片字段，指定上传路径
    image_json = models.TextField( null=True, blank=True)  # 图片json字段，示例
    islabeled = models.BooleanField(default=False)  # 是否标注字段，示例
    isailabeled = models.BooleanField(default=False)  # 是否AI标注字段，示例

    def __str__(self):
        return self.user.username + '-' + self.name