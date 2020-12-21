import uuid
from django.http import JsonResponse
from rest_framework.views import APIView

from Auth.models import UserInfo
from Auth.serializers import LoginSerializer


class LoginView(APIView):
    def post(self, request):
        print(request.data)
        # 验证前端数据
        serializer = LoginSerializer(data=request.data)
        # is_valid()判断数据是否符合要求
        if not serializer.is_valid():
            return JsonResponse(data={'login': False, 'message': '验证码错误!'}, status=400)
        # 判断用户是否创建
        # validated_data用于获取验证并处理好的数据
        phone = serializer.validated_data.get('phone')
        user_obj, flag = UserInfo.objects.get_or_create(phone=phone)
        user_obj.token = str(uuid.uuid4())
        user_obj.save()
        data = {
            'login': True,
            'token': user_obj.token,
            'phone': phone
        }
        return JsonResponse(data=data, status=200)
