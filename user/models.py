from django.db import models

from utils import base_model


class UserInfo(base_model.BaseModel):
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    nickName = models.CharField(verbose_name='昵称', max_length=16, null=True)
    username = models.CharField(verbose_name='真实姓名', max_length=16, null=True)
    age = models.IntegerField(verbose_name='年龄', default=18)
    gender = models.IntegerField(verbose_name='性别', default=0)  # 0男 1女
    avatarUrl = models.CharField(verbose_name='头像地址', null=True, max_length=1000)
    loginTime = models.DateTimeField(auto_now_add=True, verbose_name='登录时间', null=True)
    is_vistor = models.BooleanField(default=True)  # 默认是游客
    roles = models.ManyToManyField(max_length=50, verbose_name='角色', to='Role', db_table='sysuser_roles')
    service = models.ManyToManyField(verbose_name='服务', to='service.Services', db_table='user_service', db_constraint=False)

    class Meta:
        db_table = 'userinfo'


class UserToken(models.Model):
    userInfo = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    class Meta:
        db_table = "sysuser_token"
        verbose_name = '用户token信息'
        verbose_name_plural = verbose_name


class Role(base_model.BaseModel):
    name = models.CharField(max_length=50, verbose_name='角色名称', null=False)
    permissions = models.ManyToManyField(verbose_name="拥有的所有权限", to='Permission')  # , through='RolePermission')
    status = models.IntegerField(verbose_name='角色状态', default=1)  # choices=enable_status,
    need_approval = models.BooleanField(verbose_name='是否需要审核', default=True)

    operator_time = models.DateTimeField(null=True, verbose_name='操作时间')
    operator_user = models.CharField(max_length=50, null=True, verbose_name='操作人')
    operator_user_id = models.IntegerField(null=True, verbose_name='操作人id')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sysrole'
        verbose_name = '角色表'
        verbose_name_plural = verbose_name


class Permission(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='权限名称')
    code = models.CharField(max_length=10, null=True, verbose_name='权限编码')

    class Meta:
        db_table = "syspermission"
        verbose_name = '权限信息'
        verbose_name_plural = verbose_name








