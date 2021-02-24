from django.db import models

# Create your models here.
from utils import base_model


class Address(base_model.BaseModel):
    user_id = models.IntegerField(verbose_name='用户id')
    name = models.CharField(max_length=16, verbose_name='联系人')
    telphone = models.CharField(max_length=11, verbose_name='电话')
    province = models.CharField(max_length=16, verbose_name='省份')
    city = models.CharField(max_length=16, verbose_name='城市')
    location = models.CharField(max_length=16, verbose_name='地区')
    address_detail = models.TextField(verbose_name='详细地址')

    class Meta:
        db_table = 'address'