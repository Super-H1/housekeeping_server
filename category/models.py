from django.db import models

# Create your models here.
from utils import base_model


class Category(base_model.BaseModel):
    name = models.CharField(max_length=16, unique=True)
    categoryUrl = models.TextField()
    code = models.CharField(max_length=512, null=True)
    price = models.FloatField(default=0)

    class Meta:
        db_table = 'category'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name
