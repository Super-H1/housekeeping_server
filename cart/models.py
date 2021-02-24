from utils import base_model
from django.db import models

class Cart(base_model.BaseModel):

    user_id = models.IntegerField()
    good_id = models.IntegerField()
    service = models.ForeignKey(to='service.Services', db_column='good', on_delete=models.CASCADE, default=None)
    good_num = models.IntegerField(default=1)
    good_price = models.FloatField(default=None, null=True)
    is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart'