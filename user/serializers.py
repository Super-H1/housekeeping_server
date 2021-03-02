from rest_framework import serializers

from user.models import UserInfo, Role, Permission
from utils.common_utils import get_model_fields


class User_RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'status']


class MyUser_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["id", 'title', 'code']


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='姓名', max_length=16, required=False, allow_null=True, allow_blank=True)
    avatarUrl = serializers.CharField(label='头像地址', max_length=1000, required=False, allow_null=True)
    nickName = serializers.CharField(label='昵称', required=False, allow_null=True)
    age = serializers.IntegerField(label='年龄', required=False, allow_null=True)
    gender = serializers.IntegerField(label='性别', required=False)
    phone = serializers.CharField(label='手机号', max_length=11, required=False, read_only=True)
    roles = User_RoleSerializer(label='角色', required=False, many=True)
    permissions = MyUser_PermissionSerializer(label='权限', required=False, many=True)

    class Meta:
        model = UserInfo
        fields = get_model_fields(UserInfo, add_list=['roles', 'permissions'])

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
