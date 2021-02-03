from django.http import JsonResponse
from rest_framework.views import APIView

from user.models import UserInfo
from user.serializers import UserSerializer


class UserView(APIView):

    def post(self, request, pk):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(data=None, status=400, safe=False)
        user = UserInfo.objects.filter(id=pk).first()
        user_obj = serializer.update(user, serializer.validated_data)
        result = UserSerializer(user_obj)
        user_data = result.data
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
        return JsonResponse(data={'flag': True, 'user': user_data}, status=200, safe=False)
