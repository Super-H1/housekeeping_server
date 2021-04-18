from rest_framework import serializers

from collect.models import Collect
from service.models import Services
from service.serializers import ServicesSerializer
from user.models import UserInfo
from user.serializers import UserSerializer


class CollectSerializer(serializers.ModelSerializer):
    service_id = serializers.IntegerField(label='服务id')
    is_collect = serializers.BooleanField(label='是否收藏')
    user = UserSerializer(required=False)
    service = ServicesSerializer(required=False)

    class Meta:
        model = Collect
        fields = '__all__'

    def create(self, validated_data, user_id):
        user = UserInfo.objects.filter(id=user_id).first()
        service = Services.objects.filter(id=validated_data['service_id']).first()
        instance, _ = Collect.objects.update_or_create(user=user, service=service)
        instance.is_collect = validated_data['is_collect']
        instance.save()

        return instance