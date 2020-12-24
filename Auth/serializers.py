import uuid

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import UserInfo
from utils.redis_set import Res
from serializers.validators import phone_validator


class CodeSerializer(serializers.Serializer):
    # validators 自定义校验规则
    phone = serializers.CharField(required=True, validators=[phone_validator, ])


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator, ])
    code = serializers.CharField(label='短信验证码', write_only=True)
    avatarUrl = serializers.CharField(label='头像地址', max_length=1000, required=False)
    nickName = serializers.CharField(label='昵称', required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.IntegerField(required=False)

    def create(self, validated_data):
        phone = validated_data.get('phone')
        avatarUrl = str(validated_data.get('avatarUrl'))
        nickName = validated_data.get('nickName')
        user_obj, flag = UserInfo.objects.get_or_create(phone=phone)
        # 新用户要添加头像和名称
        if flag:
            user_obj.avatarUrl = avatarUrl
            user_obj.nickName = nickName
        user_obj.token = str(uuid.uuid4())
        user_obj.save()
        return user_obj

    def validate_code(self, value):
        if len(value) != 4:
            raise ValidationError('验证码错误!')
        phone = self.initial_data.get('phone')
        code_redis = Res.get(phone).decode('utf-8')
        if not code_redis:
            raise ValidationError('验证码已过期！')
        if value.lower() != code_redis.lower():
            raise ValidationError('验证码错误!')
        return value
