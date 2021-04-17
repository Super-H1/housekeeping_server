from django.db import models

from utils import base_model


# 赏金表

class Reward(base_model.BaseModel):
    user = models.OneToOneField(to='user.UserInfo', on_delete=models.CASCADE)
    money = models.FloatField(verbose_name='为发放赏金总数', default=0)
    is_grant = models.BooleanField(verbose_name='是否发放', default=False)
    total_money = models.FloatField(verbose_name='赏金总数', default=0)

    class Meta:
        db_table = 'reward'
        verbose_name = '赏金表'
        verbose_name_plural = verbose_name
