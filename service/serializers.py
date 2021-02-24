from rest_framework import serializers

from category.models import Category
from category.serializers import CategorySerializer
from service.models import Services
from utils.common_utils import get_model_fields


class ServicesSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    username = serializers.CharField(max_length=16)
    age = serializers.IntegerField()
    edu_background = serializers.CharField(max_length=50)
    marital_status = serializers.CharField(max_length=20)
    native_place = serializers.CharField(max_length=20)
    height = serializers.FloatField()
    weight = serializers.FloatField()
    experience = serializers.IntegerField()
    work_status = serializers.CharField(max_length=20, allow_null=True, required=False)
    information = serializers.CharField(max_length=1000, allow_null=True, required=False)
    training_record = serializers.CharField(max_length=1000, allow_null=True, required=False)
    work_record = serializers.CharField(max_length=1000, allow_null=True, required=False)
    servicesUrl = serializers.CharField(max_length=1000)
    userid = serializers.IntegerField(label='用户id', read_only=True)
    s_category = CategorySerializer(read_only=True)

    class Meta:
        model = Services
        fields = get_model_fields(Services, add_list=['userid'])

    def create(self, validated_data):
        category = Category.objects.filter(id=validated_data['category_id']).first()
        service_obj = None
        if category:
            service_obj = Services.objects.create(**validated_data,s_category=category)
        return service_obj
