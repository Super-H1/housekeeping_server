from utils import base_model
from django.db import models

class Services(base_model.BaseModel):
    category_id = models.IntegerField(verbose_name='分类id', null=True)
    s_category = models.ForeignKey(to='category.Category', on_delete=models.CASCADE, default=None)
    username = models.CharField(verbose_name='名字', null=True, max_length=16)
    age = models.IntegerField(verbose_name='年纪', null=True)
    edu_background = models.CharField(verbose_name='学历', max_length=16, null=True)
    marital_status = models.CharField(verbose_name='婚姻状况', max_length=16, null=True)
    native_place = models.CharField(verbose_name='籍贯', max_length=16, null=True)
    height = models.FloatField(verbose_name='身高')
    weight = models.FloatField(verbose_name='体重')
    experience = models.IntegerField(verbose_name='经验')
    work_status = models.CharField(verbose_name='工作状态', max_length=16, null=True)
    information = models.TextField(verbose_name='更多信息', null=True, default=None)
    training_record = models.TextField(verbose_name='培训记录', null=True, default=None)
    work_record = models.TextField(verbose_name='工作记录', null=True, default=None)
    servicesUrl = models.CharField(verbose_name='地址', max_length=1000, null=True)
    grade = models.IntegerField(verbose_name='服务等级', default=1)

    class Meta:
        db_table = 'services'
        verbose_name = '服务表'
        verbose_name_plural = verbose_name