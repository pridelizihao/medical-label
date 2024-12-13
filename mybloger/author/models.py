from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Captcha(models.Model):
    email = models.EmailField(unique=True,verbose_name="邮箱")
    captcha = models.CharField(max_length=4,verbose_name="验证码")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

class user_head(models.Model):
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE, related_name='user_head', null=True, blank=True, default=None)
    head_img = models.ImageField(upload_to='head_img',verbose_name="头像")
    