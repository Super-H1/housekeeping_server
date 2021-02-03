from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from service.serializers import ServicesSerializer
from user.models import Cart, Services
from utils.common_utils import get_model_fields


class CartSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(label='用户Id')
    good_id = serializers.IntegerField(label='服务Id')
    service = ServicesSerializer(read_only=True)
    good_num = serializers.IntegerField(label='数量')
    good_price = serializers.FloatField(label='商品价格')
    is_select = serializers.BooleanField(required=False, read_only=True)
    class Meta:
        model = Cart
        fields = get_model_fields(Cart)

    def create(self, validated_data):
        try:
            service = Services.objects.filter(id=validated_data['good_id']).first()
            obj, flag = Cart.objects.update_or_create(user_id=validated_data['user_id'], good_id=validated_data['good_id'], service=service)
            if validated_data['good_num'] == 0:
                obj.delete()
                return None
            obj.good_num = validated_data['good_num']
            obj.good_price = validated_data['good_price']
            obj.save()
        except Exception as e:
            raise ValidationError('创建失败')
        return obj

