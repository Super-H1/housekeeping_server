from django.http import JsonResponse
from rest_framework.views import APIView

from Auth.serializers import LoginSerializer, CodeSerializer
from reward.models import Reward
from user.serializers import UserSerializer, User_RoleSerializer
from utils.common_utils import producecode
from utils.redis_set import Res


class LoginView(APIView):

    def post(self, request):
        # 验证前端数据
        serializer = LoginSerializer(data=request.data)
        # is_valid()判断数据是否符合要求
        if not serializer.is_valid():
            return JsonResponse(data={'login': False, 'message': '验证码错误!'}, status=400)
        # 判断用户是否创建
        # validated_data用于获取验证并处理好的数据
        # 反序列化为json数据
        user_obj = serializer.create(request.data)
        Res.set('user_id', user_obj.id, ex=1393840000)
        result = UserSerializer(user_obj)
        user_data = result.data
        reward = Reward.objects.filter(user=user_obj, is_grant=True).first()
        if reward:
            user_data['reward'] = reward.total_money
        else:
            user_data['reward'] = 0
        user_roles = user_obj.roles.all()
        permissions = []
        if user_roles:
            for role in user_roles:
                ret = {
                    'id': None,
                    'title': None,
                    'code': None
                }
                permission = role.permissions.all()
                if permission:
                    for per in permission:
                        ret = {
                            'id': per.id,
                            'title': per.title,
                            'code': per.code
                        }
                        permissions.append(ret)
        user_data['permissions'] = permissions
        data = {
            'login': True,
            'user': user_data,
        }
        return JsonResponse(data=data, status=200)


class CodeView(APIView):
    def get(self, request):
        print(request.query_params)
        serializer = CodeSerializer(data=request.query_params)
        if serializer.is_valid():
            print(serializer.data)
            phone = serializer.validated_data.get('phone')
            code = producecode()
            # 设置过期时间
            key = 'House' + phone
            Res.set(key, code, ex=60 * 5)
            print('验证码：', code)
            data = {
                'code': code
            }
            return JsonResponse(data=data, status=200)
        else:
            return JsonResponse(data=None, status=400)
