from rest_framework import serializers

from address.models import Address
from utils.common_utils import get_model_fields


class AddressSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=16, read_only=True)
    name = serializers.CharField(max_length=16)
    telphone = serializers.CharField(max_length=11)
    province = serializers.CharField(max_length=16)
    city = serializers.CharField(max_length=16)
    location = serializers.CharField(max_length=16)
    address_detail = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Address
        fields = get_model_fields(Address)

    def create(self, validated_data, user_id):
        address_obj = Address.objects.create(user_id=user_id, **validated_data)
        return address_obj

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class AddressDefaultSerializer(serializers.Serializer):
    address_id = serializers.CharField()

    def set_default_address(self, queryset, validated_data):
        address_id = validated_data.pop('address_id')
        queries = queryset.filter(is_default=True)
        for obj in queries:
            obj.is_default = False
            obj.save()
        instance = queryset.filter(id=address_id).first()
        instance.is_default = True
        instance.save()
        return instance






