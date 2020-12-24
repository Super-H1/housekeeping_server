from rest_framework import serializers

from user.models import UserInfo


class UserSerializer(serializers.Serializer):
    avatarUrl = serializers.CharField(label='头像地址', max_length=1000, required=False)
    nickName = serializers.CharField(label='昵称', required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.IntegerField(required=False)
    phone = serializers.CharField(max_length=11, required=False, read_only=True)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
