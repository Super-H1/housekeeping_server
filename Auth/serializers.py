from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import UserInfo, UserToken, Role
from utils import custom_token
from utils.redis_set import Res
from serializers.validators import phone_validator


class CodeSerializer(serializers.Serializer):
    # validators 自定义校验规则
    phone = serializers.CharField(required=True, validators=[phone_validator, ])


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator, ])
    code = serializers.CharField(label='短信验证码', write_only=True)

    def create(self, validated_data):
        phone = validated_data.get('phone')
        avatarUrl = str(validated_data.get('avatarUrl'))
        nickName = validated_data.get('nickName')
        user_obj, flag = UserInfo.objects.get_or_create(phone=phone)
        token = custom_token.usertoken_md5(user_obj.phone)
        UserToken.objects.update_or_create(userInfo=user_obj, defaults={'token': token})
        # 新用户要添加头像和名称,角色，权限
        if flag:
            user_obj.avatarUrl = avatarUrl
            user_obj.nickName = nickName
            user_obj.is_vistor = False
            role = Role.objects.filter(name='common_user').first()
            user_obj.roles.add(role)
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

