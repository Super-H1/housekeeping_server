from django.db import models

from utils import base_model


class Collect(base_model.BaseModel):
    service = models.ForeignKey(to='service.Services', on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.UserInfo', on_delete=models.CASCADE)
    is_collect = models.BooleanField(default=True)

    class Meta:
        db_table = 'collect'
        verbose_name = '收藏表'
        verbose_name_plural = verbose_name
