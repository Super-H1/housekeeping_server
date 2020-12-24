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
        user = serializer.update(user, serializer.validated_data)
        result = UserSerializer(user)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200, safe=False)
