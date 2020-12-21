from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from utils.redis_set import Res
from serializers.validators import phone_validator



class CodeSerializer(serializers.Serializer):
    # validators 自定义校验规则
    phone = serializers.CharField(required=True, validators=[phone_validator, ])


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, validators=[phone_validator, ])
    code = serializers.CharField(required=True, label='短信验证码')

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


