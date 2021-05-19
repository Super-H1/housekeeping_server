import datetime

from django.db.models import Q
from rest_framework import serializers

from address.models import Address
from cart.models import Cart
from order.models import Order, OrderService
from service.models import Services
from utils.common_utils import get_model_fields, get_num


class Order_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name', 'telphone', 'province', 'city', 'location', 'address_detail']


class Order_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    OrderNumber = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    service_num = serializers.IntegerField()
    service_unit = serializers.CharField(read_only=True)
    status = serializers.IntegerField(read_only=True)
    address = Order_addressSerializer(read_only=True)
    price = serializers.FloatField()
    point = serializers.IntegerField(read_only=True)
    payment = serializers.IntegerField(read_only=True)
    is_evaluate = serializers.IntegerField(read_only=True)
    is_complian = serializers.IntegerField(read_only=True)
    address_id = serializers.IntegerField(write_only=True)
    cart_id = serializers.ListField(write_only=True)

    class Meta:
        model = Order
        fields = get_model_fields(Order, add_list=['address_id', 'cart_id'])

    def create(self, validated_data, user_id):
        service_num = validated_data.pop('service_num')
        address_id = validated_data.pop('address_id')
        price = validated_data.pop('price')
        cart_id_list = validated_data.pop('cart_id')
        address_obj = Address.objects.filter(id=address_id).first()
        year = datetime.datetime.now().year
        q1_creation_time = Q(creation_time__lte=datetime.datetime(year, 12, 31, 23, 59, 59))
        q2_creation_time = Q(creation_time__gte=datetime.datetime(year, 1, 1))
        orders = Order.objects.filter((q1_creation_time & q2_creation_time)).order_by('-creation_time').all()
        count = 0
        if orders:
            order = orders.first()
            max_number = order.OrderNumber
            count = int(max_number[11:])
        new_count = count + 1
        OrderNumber = get_num(year, new_count)
        order_obj = Order.objects.create(user_id=user_id, OrderNumber=OrderNumber, price=price, service_num=service_num,
                                         address=address_obj)
        for cart_id in cart_id_list:
            cart_obj = Cart.objects.filter(id=cart_id).first()
            OrderService.objects.create(order=order_obj, service=cart_obj.service,
                                        o_service_num=cart_obj.good_num, service_price=cart_obj.good_price)
            # 清空购物车
            cart_obj.delete()

        return order_obj


class OrderServiceSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    service = Order_serviceSerializer()
    o_service_num = serializers.IntegerField()
    service_price = serializers.FloatField()

    class Meta:
        model = OrderService
        fields = '__all__'
