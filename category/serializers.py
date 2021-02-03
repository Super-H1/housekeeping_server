from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from category.models import Category
from utils.common_utils import get_model_fields


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='分类名称', max_length=16)
    categoryUrl = serializers.CharField(label='图片地址', max_length=1000)
    code = serializers.CharField(label='分类编号', max_length=16)
    price = serializers.FloatField(label='价格')
    class Meta:
        model = Category
        fields = get_model_fields(Category)


    def create(self, validated_data):
        try:
            category_obj = Category.objects.create(**validated_data)
        except Exception as e:
            raise ValidationError('重复创建')
        return category_obj
