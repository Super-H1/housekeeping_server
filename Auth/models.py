from django.db import models


class UserInfo(models.Model):
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    nickName = models.CharField(verbose_name='昵称', max_length=16, null=True)
    age = models.IntegerField(verbose_name='年龄', default=18)
    gender = models.IntegerField(verbose_name='性别', default=0)  # 0男 1女
    avatarUrl = models.CharField(verbose_name='头像地址', null=True, max_length=1000)
    token = models.CharField(verbose_name='用户token', max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'userinfo'
