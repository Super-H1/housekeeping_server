from rest_framework import serializers

from address.models import Address
from utils.common_utils import get_model_fields


class AddressSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=16)
    telphone = serializers.CharField(max_length=11)
    province = serializers.CharField(max_length=16)
    city = serializers.CharField(max_length=16)
    location = serializers.CharField(max_length=16)
    address_detail = serializers.CharField()

    class Meta:
        model = Address
        fields = get_model_fields(Address)

    def create(self, validated_data, user):
        address_obj = Address.objects.update_or_create(user_id=user.id, **validated_data)
        return address_obj


