from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

#用户信息
class User(AbstractUser):
    #电话号码
    mobile = models.CharField(max_length=11, unique=True, blank=False)

    #头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d', blank=True)

    #个人简介
    user_desc = models.TextField(max_length=500, blank=True)

    #修改认证的字段
    USERNAME_FIELD = 'mobile'

    #创建超级管理员的需要 必须输入的字段(不包含手机号和密码)
    REQUIRED_FIELDS = ['username', 'email']

    #内部类 class Meta 用于给model定义元数据
    class Meta:
        db_table = 'tb_users'    #修改默认的表名
        verbose_name = '用户信息'   #Admin后台显示
        verbose_name_plural = verbose_name      #Admin后台显示

    def __str__(self):
        return self.mobile


