import re
from rest_framework.exceptions import ValidationError

# 用于前端字段校验

def phone_validator(value):
    flag_phone = re.match(r'^(((13[0-9]{1})|(15[0-9]{1})|(19[0-9]{1})|(18[0-9]{1})|(17[0-9]{1}))+\d{8})$', value)
    if not flag_phone:
        raise ValidationError("手机号错误！")