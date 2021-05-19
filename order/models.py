from django.db import models

from utils.base_model import BaseModel


class Order(BaseModel):
    OrderNumber = models.CharField(verbose_name='订单编号', max_length=512, default=None)
    user_id = models.IntegerField(verbose_name='用户id')
    service_num = models.IntegerField(verbose_name='商品总数量')
    service_unit = models.CharField(verbose_name='单位', max_length=16, default='小时')
    status = models.IntegerField(verbose_name='订单状态', default=0)  # 0待支付 10支付成功 20待评价 30支付失败
    address = models.ForeignKey(verbose_name='配送地址', to='address.Address', default=None, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='商品总价')
    point = models.FloatField(verbose_name='赠送积分', default=5)
    payment = models.IntegerField(verbose_name='支付方式', default=1)  # 1微信支付 2支付宝支付
    is_evaluate = models.BooleanField(verbose_name='是否评价', default=False)
    is_complian = models.BooleanField(verbose_name='是否投诉', default=False)

    class Meta:
        db_table = 'order'


class OrderService(models.Model):
    order = models.ForeignKey(to='order.Order', db_column='order_id', on_delete=models.CASCADE)
    service = models.ForeignKey(to='service.Services', db_column='service_id', on_delete=models.CASCADE)
    service_price = models.FloatField(verbose_name='服务单价', default=None)
    o_service_num = models.IntegerField(verbose_name='服务数量', default=1)
    class Meta:
        db_table = 'order_service'


