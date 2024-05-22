from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """用户表"""
    # id = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=100)
    password = models.IntegerField(default=0)
    search_count = models.IntegerField(default=0)
    remain_count = models.IntegerField(default=10)
    regist_date = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=100, default='')

# UserInfo.objects.create() id自增


"""
加一个查询记录表
"""
